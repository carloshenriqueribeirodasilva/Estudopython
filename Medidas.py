medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media de {}m corresponde a {}cm e {}mm {}dm {}dam {}hm {}km'.format(medida, cm, mm, dm, dam, hm, km))