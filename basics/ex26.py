line1 = "РћС€РёР±РєР° РІР°Р»РёРґР°С†РёРё XML. РљРѕР»РёС‡РµСЃС‚РІРѕ: 10"
line2 = "SubNetwork=Root,SubNetwork=DU,MeContext=MSK183-DU Р’Р°Р»РёРґР°С†РёСЏ XML ..."
line3 = "UploadXml Р·Р°РїСЂРѕСЃ РѕР±СЂР°Р±РѕС‚Р°РЅ СѓСЃРїРµС€РЅРѕ"
line4 = "<upload_xml> РџРѕСЃР»Р°РЅРѕ РІ РѕС‡РµСЂРµРґСЊ"
line5 = "UploadXml РѕС‚РїСЂР°РІР»СЏРµРј Р·Р°РїСЂРѕСЃ..."

upd_line_1 = line1.encode("windows-1251").decode("utf-8")
upd_line_2 = line2.encode("windows-1251").decode("utf-8")
upd_line_3 = line3.encode("windows-1251").decode("utf-8")
upd_line_4 = line4.encode("windows-1251").decode("utf-8")
upd_line_5 = line5.encode("windows-1251").decode("utf-8")

print(upd_line_1, upd_line_2, upd_line_3, upd_line_4, upd_line_5, end="\n")
