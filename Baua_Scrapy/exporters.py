from scrapy.exporters import CsvItemExporter

"""Customize the CSV exportation with ';' delimiter

"""
class CsvCustomSeperator(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = ';'
        super(CsvCustomSeperator, self).__init__(*args, **kwargs)