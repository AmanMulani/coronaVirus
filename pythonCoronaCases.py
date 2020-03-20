import coronavirus as coniv 
import asyncio
import time

#This class is used to store the data of the country, whose details we want to find out.
class StoreData():
	def __init__(self, country, totalCases, recovered, deaths):
		self.country = country
		self.totalCases = totalCases
		self.recovered = recovered
		self.deaths = deaths

	def __str__(self):
		return "Country: {}\nNo. of Cases: {}\nNo of patients recovered: {}\nTotal Number of deaths: {}".format(self.country, self.totalCases, self.recovered, self.deaths)

	#calculate() is used to find the mortality and the recovery rate.
	def calculate(self):
		recoveryRate = self.recovered/self.totalCases * 100
		mortalityRate = self.deaths/self.totalCases * 100
		print('Recovery Rate: {0}%'.format(recoveryRate))
		print('Mortality Rate: {0}%'.format(mortalityRate))


#connecting to the client server to fetch the information
async def getCases():
	print('Fetching data from server....')
	session = coniv.ClientSession()
	cases = await coniv.get_cases(session)
	await session.close()
	flag = 0
	target_country = input('Enter the country whose data you want to access.\n')
	time.sleep(1 )
	print('Feteched Data---->')
	for count in cases:
		if count.country == target_country:
			data = StoreData(target_country, count.confirmed, count.recovered, count.deaths)
			flag = 1
			break

	if flag == 1:
		print(data)
		data.calculate()
		print('COVID-19 is preventable, so take care.')
		print('Follow the guidelines issued by your country.')

	else:
		print('No Cases in your country. Don\'t panic, just be alert.')
		print('Have a nice day.')

async def main():
	cases = await asyncio.gather(getCases())

asyncio.run(main())









