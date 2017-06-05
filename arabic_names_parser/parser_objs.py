# -*- coding: utf-8 -*-
from parser_utils import Astr

#### Defining here which are the words which signal the beginning of a particular part of the name.

nasab_dict ={Astr('بن '): ['bin', 'ben', 'ibn'],
             Astr('بنت '): ['bint']}

kunya_dict = {Astr('أبو '): ['abu'],
			  Astr('ابو '): ['abu'],
              Astr('أم '): ['umm', 'oum'],
              Astr('أوم '): ['umm', 'oum']}

nisbah_dict = {Astr('من_ال_'): ['of the']}

name_part_dict = {'nasab': nasab_dict, 'kunya': kunya_dict, 'nisbah': nisbah_dict}


#### Defininig here the arabic words which should be aggregated to the following.

al_list = [Astr('آل '), Astr('ال '), Astr('من ')]
abdul_list = [Astr('عبد '), Astr('عبدو '), Astr('أبدول '), Astr('أبدل ')]
master_list = [Astr('السيد '), Astr('سيد '), Astr('السيدة ')]

concat_list = al_list + abdul_list + master_list


#####Copy pasting the particular lists for the arabic parser for speed reasons.

laqab_M = ['\xef\xbb\xbf\xd8\xa7\xd9\x84\xd8\xa3\xd8\xa8\xd8\xb1\xd8\xa7\xd8\xb4', '\xd8\xa7\xd9\x84\xd8\xb9\xd8\xaf\xd9\x88\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb9\xd9\x88\xd8\xa7\xd8\xb1', '\xd8\xa7\xd9\x84\xd8\xaf\xd8\xb1\xd9\x8a\xd8\xb1', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd9\x8a\xd8\xa8', '\xd8\xa2\xd9\x84 \xd8\xa7\xd9\x84\xd8\xac\xd8\xb9\xd8\xaf', '\xd8\xa7\xd9\x84\xd9\x83\xd8\xa8\xd9\x8a\xd8\xb1', '\xd8\xa7\xd9\x84\xd9\x83\xd9\x84\xd8\xa8\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x86\xd8\xa8\xd9\x8a\xd9\x84', '\xd8\xa7\xd9\x84\xd9\x86\xd8\xb5\xd8\xb1\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb1\xd8\xb4\xd9\x8a\xd8\xaf', '\xd8\xa7\xd9\x84\xd8\xb5\xd9\x81\xd8\xa7\xd8\xb1', '\xd8\xa7\xd9\x84\xd8\xb5\xd8\xba\xd9\x8a\xd8\xb1', '\xd8\xa2\xd9\x84 \xd8\xa7\xd9\x84\xd8\xb4\xd8\xb9\xd8\xa8\xd9\x8a\xd8\x8c', '\xd8\xa2\xd9\x84 \xd8\xa7\xd9\x84\xd8\xb3\xd9\x83\xd8\xb1\xd9\x8a\xd8\xa9', '\xd8\xa7\xd9\x84\xd9\x84\xd9\x87 \xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb7\xd9\x8a\xd8\xa8', '\xd8\xa7\xd9\x84\xd8\xb2\xd9\x87\xd8\xb1\xd9\x8a']
laqab_F = ['\xef\xbb\xbf\xd8\xa7\xd9\x84\xd8\xb2\xd8\xb1\xd9\x82\xd8\xa7\xd8\xa1']
nisbah_M = ['\xd8\xa7\xd9\x84\xd8\xa3\xd8\xa8\xd8\xa7\xd8\xb1\xd8\xb7\xd8\xa7\xd8\xa6\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa7\xd8\xb3\xd8\xaa\xd8\xb1\xd9\x84\xd8\xa7\xd8\xa8\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb7\xd8\xa7\xd8\xb1', '\xd8\xa7\xd9\x84\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xb9\xd9\x84\xd8\xa8\xd9\x83\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xba\xd8\xaf\xd8\xa7\xd8\xaf\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xb1\xd8\xa8\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xb5\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xae\xd8\xa7\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa8\xd8\xb1\xd8\xac\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xaf\xd9\x84\xd9\x8a\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xaf\xd9\x85\xd8\xb4\xd9\x82\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xba\xd8\xb3\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd9\x84\xd8\xac', '\xd8\xa7\xd9\x84\xd8\xad\xd9\x85\xd8\xaf\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd9\x85\xd8\xaf\xd9\x88\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xb1\xd8\xa8\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xa7\xd8\xb1\xd8\xab', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xa7\xd8\xb1\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x87\xd8\xa7\xd8\xb4\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xac\xd8\xa7\xd8\xb2\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd9\x85\xd8\xb5\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x87\xd9\x86\xd8\xaf\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd9\x8a\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa7\xd9\x81\xd8\xb1\xd9\x8a\xd9\x82\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa5\xd8\xae\xd9\x85\xd9\x8a\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa5\xd8\xb3\xd8\xa8\xd9\x87\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xa7\xd8\xb3\xd9\x83\xd8\xa7\xd9\x81\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xac\xd9\x87\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xac\xd8\xb1\xd8\xa7\xd8\xb4\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x83\xd8\xb1\xd8\xae\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x83\xd8\xa7\xd8\xaa\xd8\xa8', '\xd8\xa7\xd9\x84\xd8\xae\xd9\x8a\xd8\xa7\xd8\xb7', '\xd8\xa7\xd9\x84\xd8\xae\xd8\xb1\xd8\xa7\xd8\xb3\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xae\xd9\x88\xd8\xa7\xd8\xb1\xd8\xb2\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x83\xd9\x88\xd9\x81\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x84\xd8\xb9\xd9\x84\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd8\xaf\xd8\xa7\xd8\xa6\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd8\xaf\xd9\x8a\xd9\x86\xd8\xa9 \xd8\xa7\xd9\x84\xd9\x85\xd9\x86\xd9\x88\xd8\xb1\xd8\xa9', '\xd8\xa7\xd9\x84\xd9\x85\xd8\xba\xd8\xb1\xd8\xa8\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd8\xae\xd8\xb2\xd9\x88\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd9\x83\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd9\x88\xd8\xb5\xd9\x84\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x85\xd8\xb5\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x86\xd9\x87\xd8\xb1\xd8\xaa\xd9\x8a\xd8\xb1\xd9\x8a', '\xd9\x86\xd8\xa7\xd8\xac\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x86\xd8\xac\xd8\xa7\xd8\xb1', '\xd8\xa7\xd9\x84\xd9\x86\xd8\xa7\xd9\x8a\xd8\xb3\xd8\xa7\xd8\xa8\xd9\x88\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x82\xd8\xb7\xd8\xa7\xd9\x86', '\xd8\xa7\xd9\x84\xd9\x82\xd9\x8a\xd8\xb1\xd9\x88\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb1\xd8\xa7\xd9\x87\xd8\xa8', '\xd8\xa7\xd9\x84\xd8\xb1\xd8\xb4\xd9\x8a\xd8\xaf\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb1\xd9\x88\xd8\xa7\xd9\x86\xd8\xaf\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb1\xd9\x88\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd8\xae\xd8\xa7\xd9\x88\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd8\xae\xd8\xaa\xd9\x8a\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa7\xd9\x85\xd8\xb1\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb4\xd8\xb9\xd8\xb1\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb4\xd9\x8a\xd8\xb1\xd8\xa7\xd8\xb2\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd9\x8a\xd8\xb3\xd8\xaa\xd8\xa7\xd9\x86\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb5\xd9\x88\xd9\x81\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb7\xd8\xa7\xd9\x87\xd8\xb1\xd9\x8a', '\xd8\xa2\xd9\x84 \xd8\xaa\xd8\xa7\xd8\xb1\xd9\x8a\xd8\xae\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb9\xd9\x82\xd9\x84\xd9\x8a\xd8\xaf\xd9\x8a', '\xd8\xa7\xd9\x84\xd9\x88\xd8\xb3\xd9\x8a\xd8\xb7\xd9\x8a', '\xd8\xa7\xd9\x84\xd8\xb2\xd8\xa8\xd9\x8a\xd8\xb1\xd9\x8a']


#Converting Arabic Presentation Objects to classic arabic letters
#https://stackoverflow.com/questions/39415720/how-to-convert-arabic-presentation-forms-b-to-normal-arabic-characters-with-bash

arabic_forms_toclassic_lookup = {u'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎ':u'ا',
								u'ﺏﺐﺑﺒ':u'ب',
								u'ﺓﺔ':u'ه',
								u'ﺕﺖﺗﺘ':u'ت',
								u'ﺙﺚﺛﺜ':u'ث',
								u'ﺝﺞﺟﺠ':u'ج',
								u'ﺡﺢﺣﺤ':u'ح',
								u'ﺥﺦﺧﺨ':u'خ',
								u'ﺩﺪ':u'د',
								u'ﺫﺬ':u'ذ',
								u'ﺭﺮ':u'ر',
								u'ﺯﺰ':u'ز',
								u'ﺱﺲﺳﺴ':u'س',
								u'ﺵﺶﺷﺸ':u'ش',
								u'ﺹﺺﺻﺼ':u'ص',
								u'ﺽﺾﺿﻀ':u'ض',
								u'ﻁﻂﻃﻄ':u'ط',
								u'ﻅﻆﻇﻈ':u'ظ',
								u'ﻉﻊﻋﻌ':u'ع',
								u'ﻍﻎﻏﻐ':u'غ',
								u'ﻑﻒﻓﻔ':u'ف',
								u'ﻕﻖﻗﻘ':u'ق',
								u'ﻙﻚﻛﻜ':u'ك',
								u'ﻝﻞﻟﻠ':u'ل',
								u'ﻡﻢﻣﻤ':u'م',
								u'ﻥﻦﻧﻨ':u'ن',
								u'ﻩﻪﻫﻬ':u'ه',
								u'ﻭﻮ':u'و',
								u'ﻯﻰﻱﻲﻳﻴ':u'ي',
								u'ﻵﻶﻷﻸﻹﻺﻻﻼ':u'لا'}


if __name__ == '__main__':
	print len(laqab_F), len(laqab_M), len(nisbah_M)
