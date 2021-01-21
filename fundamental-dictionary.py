"""
dictionary
"""

kamus = {'father': 'ayah', 'mother': 'mama', 'anak': 'son', 'child': 'anak-anak'}
print(kamus)
print(kamus['father'])
print(kamus['mother'])
print(kamus['anak'])
print(kamus['child'])

print('\n')
print('data ini dikirmkan oleh server gojek, untuk memberikan info driver di sekitar aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-06-10',
    'driver_list' : ['eko', 'dwi', 'tri', 'catur']
     }
print(data_dari_server_gojek)
print(f'driver di sekitar sini adalah {data_dari_server_gojek["driver_list"]}')
print(f'driver terdekat di sekitar sini adalah Mas {data_dari_server_gojek["driver_list"][0]}')

print('\n')
kamus = {}
kamus ['father'] = 'ayah'
kamus ['mother'] = 'ibu'
kamus ['sister'] = 'saudari'

print (kamus)
print(kamus['father'])
print(kamus['sister'])

print('\n')
dicti = {
    'father' : 'bapak',
    'mother' : 'mama',
    'sister': 'saudariiiii',
    'brother' : 'saudarakuu'}
print(dicti)
print(dicti['father'])
print(dicti['brother'])
print(dicti['sister'])

print('\n')
print('data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_battu_server_gojek = {
    'tanggal' : '2021-01-17',
    'driver_list' :  ['eko', 'dwi', 'tri', 'catur']
}
print(data_battu_server_gojek)
print(f'driver di sekitar sini {data_battu_server_gojek["driver_list"]} ')
print(f'driver di sekitar sini adalah {data_battu_server_gojek["driver_list"][0]} ')

print('\n')
print('data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_battu_server_gojek = {
    'tanggal' : '2021-01-17',
    'driver_list' :  [{'nama' : 'eko', 'jarak' : 10},
                      {'nama':'dwi', 'jarak': 30},
                      {'nama':'tri', 'jarak': 100},
                      {'nama':'catur', 'jarak' : 1000}],
    'driver_listt' : ['eko', 'dwi', 'tri', 'catur','limo']
}
print(data_battu_server_gojek)
print(f'\ndriver di sekitar sini {data_battu_server_gojek["driver_list"]} ')
print(f'driver terdekat di sekitar sini adalah {data_battu_server_gojek["driver_list"][0]} ')
print(f'driver terjauh di sekitar sini adalah {data_battu_server_gojek["driver_list"][3]} ')

print(f"\ndriver terdekat berjarak {data_battu_server_gojek['driver_list'][0]['jarak']} meter")
print(f"driver terjauh berjarak {data_battu_server_gojek['driver_list'][3]['jarak']} meter")
