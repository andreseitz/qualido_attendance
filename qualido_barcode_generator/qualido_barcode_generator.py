import xlrd
import barcode
import os
import shutil
import argparse
from jinja2 import Template, Environment, FileSystemLoader
import subprocess

#path = "~/Downloads/export.xlsx"

class InvalidExcelFormatException(Exception):
    
    def __init__(self, message = "Excel table does not follow format assumption."):
        self.message = message

class NoUserDataException(Exception):

    def __init__(self, message = "Excel table is not filled with more than header information."):
        self.message = message 

### excel parsing

def get_sheet(path):
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(0)
    return sheet

def get_header(sheet):
    return sheet.row_values(1)

def sheet_contains_valid_header(sheet):
    header = get_header(sheet)
    try:
        header.index(u'ID')
        header.index(u'Nachname')
        header.index(u'Vorname')
    except:
        return False
    else:
        return True

def collect_relevant_columns(sheet):
    header = get_header(sheet)
    return {
        'id' : header.index(u'ID'),
        'lastname' : header.index(u'Nachname'),
        'surname' : header.index(u'Vorname')
    }

def extractUserData(sheet):
    map = collect_relevant_columns(sheet)
    users = []
    for irow in range(2,sheet.nrows):
        users.append({
            'id' : sheet.cell_value(irow, map['id']),
            'lastname' : sheet.cell_value(irow, map['lastname']),
            'surname' : sheet.cell_value(irow, map['surname'])
        })
    return users

def sheet_contains_data(sheet):
    if sheet.nrows > 2:
        return True
    else:
        return False

def parseUserData(path):
    sheet = get_sheet(path)

    if not sheet_contains_valid_header(sheet):
        raise InvalidExcelFormatException()
    
    if not sheet_contains_data(sheet):
        raise NoUserDataException()

    users = extractUserData(sheet)
    return users

### barcode generation

def prepare_barcode_target():
    if os.path.exists('barcodes'):
        shutil.rmtree('barcodes')
    os.mkdir('barcodes')

def generate_barcode(code_factory, id):
    code = code_factory(id, barcode.writer.ImageWriter())
    code.save(os.path.join('barcodes',id))

def generate_user_barcodes(users):
    code_factory = barcode.get('code128')
    for user in users:
        generate_barcode(code_factory, user['id'])

### catalogue templating

def render_template(users):
    environment = Environment(loader=FileSystemLoader("./tex/"))
    template = environment.get_template("catalogue.tex.j2")
    out = template.render(users=users)
    with open("./tex/catalogue.tex", "w") as fh:
        fh.write(out)
    fh.close()

### compile tex

def compile_catalogue():
    curdir = os.curdir
    os.chdir("./tex/")
    process = subprocess.Popen(['pdflatex', '-interaction=nonstopmode', 'catalogue.tex'])
    os.chdir(curdir)

### main

#TODO read arguments: excel path

def main():

    parser = argparse.ArgumentParser(description='Generate barcodes for Qualido users.')
    parser.add_argument(
        '-p', '--path', 
        default='export.xlsx',
        help='path to exported list of excel users')

    args = parser.parse_args()
    
    users = parseUserData(args.path)
    prepare_barcode_target()
    generate_user_barcodes(users)
    
    render_template(users)
    compile_catalogue()

    


if __name__ == '__main__':
    main()