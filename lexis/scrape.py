import re
import os
import lxml.html
from datetime import datetime


sections = [
    "Voters_EXPSEC_VTR",
    "PAWSection_EXPSEC_PAW",
    "PhonesPluses_EXPSEC_PhonPlus",
    "ProfLicSection_EXPSEC_ProfLic",
    "PossEduSection_EXPSEC_PossEdu"
]

html_file = '/Nexis Public Records_files/entrypoint.html'
results = f'{datetime.now().date().strftime("%d_%m_%Y")}.csv'

for filename in os.listdir(os.getcwd()):
    if os.path.isdir(filename):
        path = (f'{os.getcwd()}/{filename}{html_file}')
        with open(path, 'r') as f:
            html = f.read()
            tree = lxml.html.fromstring(html)
            text = ""

            for td in tree.xpath('//div[@class="SectionData"]/div[@class="reportSection"][2]/table[1]/tbody/tr[2]/td'):
                if td.text is not None:
                    text += ' ' + td.text

            for td in tree.xpath('//div[@id="Addresses_EXPSEC_AddrSum"]/div[2]/table/tbody/tr/td/div'):
                if td.text is not None:
                    text += ' ' + td.text

            for s in sections:
                xpath = f'//div[@id="{s}"]/table/tbody/tr/td'
                for td in tree.xpath(xpath):
                    if td.text is not None:
                        text += ' ' + td.text

            # to find all phone numbers
            phone_list = re.findall(r'\([0-9]{3,}\) [0-9]{3,}\-[0-9]{4,}', text)
            with open(results, 'a+') as res:
                res.write('\n\n' + filename + '\n')
                res.write('\n'.join(set(phone_list)))
