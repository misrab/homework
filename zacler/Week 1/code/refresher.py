

temp = 20

if temp <= 32:
	print "water is ice"
elif temp > 32 and temp < 212:
	print "water is liquid"
else:
	print "water will boil"

zac = {
	"name": "Zac Ler",
	"age": 24,
	"location": "Singapore",
	"gender" : "male",
	"occupation": "undergraduate"
}

minyan = {
	"name": "Min yan",
	"age": 21,
	"location": "Singapore",
	"gender" : "female",
	"occupation": "sophomore"
}

print zac['gender']

smuggers = [zac, minyan]

for smugger in smuggers:
	print type(smugger)
	print smugger['name']
	for key, value in smugger.items():
		print key+":"+ str(value)

# list comprehension

tada = [1,5,6,7,2]
print len(tada)
print [n**2 for n in tada]

# finding right angled triangles

t1 = [3,4,5]
t2 = [1,1,1]

tris = [t1,t2]

right_angles = [triangle in tris if triangle[0]**2 + triangle[1]**2 ==  triangle[2]**2]
print right_angles