from django.shortcuts import render
import pandas as pd
import numpy as np
from collections import OrderedDict
from paymentTypes.fusioncharts import FusionCharts
from paymentTypes.forms import filterData

def getNETCNationalAverage(df,year,month):
	avgDict = {}
	for i in range(1,df.shape[1]-1):
		if year == 2017:
			values = df.iloc[:12, i]
			values = list(values)
			requiredVal = float(values[month-1].rstrip('%'))
			statename = df.columns[i] 
			avgDict[statename] = requiredVal   
		      
		elif year == 2018:
			values = df.iloc[12:24, i]
			values = list(values)
			requiredVal = float(values[month-1].rstrip('%'))
			statename = df.columns[i] 
			avgDict[statename] = requiredVal    
		elif year == 2019:
			values = df.iloc[24:36, i]
			values = list(values)
			requiredVal = float(values[month-1].rstrip('%'))
			statename = df.columns[i] 
			avgDict[statename] = requiredVal     
		else:
			values = df.iloc[36:42, i]
			values = list(values)
			flval = np.zeros(12)
			requiredVal = float(values[month-1].rstrip('%'))
			statename = df.columns[i] 
			avgDict[statename] = requiredVal    

	allValues = list(avgDict.values())
	nparr = np.array(allValues)
	return np.mean(nparr)

def getUPINFSPOSNationalAverage(df,year,month):
	avgDict = {}
	for i in range(df.shape[0]):
		if year == 2017:
			allValues = df.iloc[i,1:25]
			allValues = list(allValues)
			countValues = allValues[0:25:2]
			amountValues = allValues[1:25:2]
			req1 = float(countValues[month-1].rstrip('%'))
			req2 = float(amountValues[month-1].rstrip('%'))
			name = df.iloc[i,0:1].values[0]     
			name = name.lstrip('0')
			name = name.title()
			if name == "Jammu And Kashmir":
				name = "Jammu and Kashmir"
			elif name == "Dadra And Nagar Haveli":
				name = "Dadra and Nagar Haveli"
			elif name == "Andaman And Nicobar Islands":
				name = "Andaman and Nicobar Islands"
			elif name == "Daman And Diu":
				name = "Daman and Diu"
			else:
				pass
			avgDict[name] = [req1,req2]

		elif year == 2018:
			allValues = df.iloc[i,25:49]
			allValues = list(allValues)
			countValues = allValues[0:25:2]
			amountValues = allValues[1:25:2]
			req1 = float(countValues[month-1].rstrip('%'))
			req2 = float(amountValues[month-1].rstrip('%'))
			name = df.iloc[i,0:1].values[0]     
			name = name.lstrip('0')
			name = name.title()
			if name == "Jammu And Kashmir":
				name = "Jammu and Kashmir"
			elif name == "Dadra And Nagar Haveli":
				name = "Dadra and Nagar Haveli"
			elif name == "Andaman And Nicobar Islands":
				name = "Andaman and Nicobar Islands"
			elif name == "Daman And Diu":
				name = "Daman and Diu"
			else:
				pass
			avgDict[name] = [req1,req2]
			avgDict[name] = [req1,req2]

		elif year == 2019:
			allValues = df.iloc[i,49:73]
			allValues = list(allValues)
			countValues = allValues[0:25:2]
			amountValues = allValues[1:25:2]
			req1 = float(countValues[month-1].rstrip('%'))
			req2 = float(amountValues[month-1].rstrip('%'))
			name = df.iloc[i,0:1].values[0]     
			name = name.lstrip('0')
			name = name.title()
			if name == "Jammu And Kashmir":
				name = "Jammu and Kashmir"
			elif name == "Dadra And Nagar Haveli":
				name = "Dadra and Nagar Haveli"
			elif name == "Andaman And Nicobar Islands":
				name = "Andaman and Nicobar Islands"
			elif name == "Daman And Diu":
				name = "Daman and Diu"
			else:
				pass
			avgDict[name] = [req1,req2]
			avgDict[name] = [req1,req2]

		else:
			allValues = df.iloc[i,73:83]
			allValues = list(allValues)
			countValues = allValues[0:25:2]
			amountValues = allValues[1:25:2]
			req1 = float(countValues[month-1].rstrip('%'))
			req2 = float(amountValues[month-1].rstrip('%'))
			name = df.iloc[i,0:1].values[0]     
			name = name.lstrip('0')
			name = name.title()
			if name == "Jammu And Kashmir":
				name = "Jammu and Kashmir"
			elif name == "Dadra And Nagar Haveli":
				name = "Dadra and Nagar Haveli"
			elif name == "Andaman And Nicobar Islands":
				name = "Andaman and Nicobar Islands"
			elif name == "Daman And Diu":
				name = "Daman and Diu"
			else:
				pass
			avgDict[name] = [req1,req2]
			avgDict[name] = [req1,req2]

	allValues = list(avgDict.values())
	nparr = np.array(allValues)
	return np.mean(nparr)




def getNETCDetails(df,year,month):
  avgDict = {}
  for i in range(1,df.shape[1]-1):
    if year == 2017:
      values = df.iloc[:12, i]
      values = list(values)
      requiredVal = float(values[month-1].rstrip('%'))
      statename = df.columns[i] 
      avgDict[statename] = requiredVal   
          
    elif year == 2018:
      values = df.iloc[12:24, i]
      values = list(values)
      requiredVal = float(values[month-1].rstrip('%'))
      statename = df.columns[i] 
      avgDict[statename] = requiredVal    
    
    elif year == 2019:
      values = df.iloc[24:36, i]
      values = list(values)
      requiredVal = float(values[month-1].rstrip('%'))
      statename = df.columns[i] 
      avgDict[statename] = requiredVal     
      
    else:
      values = df.iloc[36:42, i]
      values = list(values)
      flval = np.zeros(12)
      requiredVal = float(values[month-1].rstrip('%'))
      statename = df.columns[i] 
      avgDict[statename] = requiredVal    

  return avgDict


def getUPINFSPOSDetails(df,year,month):
  avgDict = {}
  for i in range(df.shape[0]):
    if year == 2017:
      allValues = df.iloc[i,1:25]
      allValues = list(allValues)
      countValues = allValues[0:25:2]
      amountValues = allValues[1:25:2]
      req1 = float(countValues[month-1].rstrip('%'))
      req2 = float(amountValues[month-1].rstrip('%'))
      name = df.iloc[i,0:1].values[0]     
      name = name.lstrip('0')
      name = name.title()
      if name == "Jammu And Kashmir":
      	name = "Jammu and Kashmir"
      elif name == "Dadra And Nagar Haveli":
      	name = "Dadra and Nagar Haveli"
      elif name == "Andaman And Nicobar Islands":
      	name = "Andaman and Nicobar Islands"
      elif name == "Daman And Diu":
      	name = "Daman and Diu"
      else:
      	pass
      avgDict[name] = [req1,req2]

    elif year == 2018:
      allValues = df.iloc[i,25:49]
      allValues = list(allValues)
      countValues = allValues[0:25:2]
      amountValues = allValues[1:25:2]
      req1 = float(countValues[month-1].rstrip('%'))
      req2 = float(amountValues[month-1].rstrip('%'))
      name = df.iloc[i,0:1].values[0]     
      name = name.lstrip('0')
      name = name.title()
      if name == "Jammu And Kashmir":
      	name = "Jammu and Kashmir"
      elif name == "Dadra And Nagar Haveli":
      	name = "Dadra and Nagar Haveli"
      elif name == "Andaman And Nicobar Islands":
      	name = "Andaman and Nicobar Islands"
      elif name == "Daman And Diu":
      	name = "Daman and Diu"
      else:
      	pass
      avgDict[name] = [req1,req2]

    elif year == 2019:
      allValues = df.iloc[i,49:73]
      allValues = list(allValues)
      countValues = allValues[0:25:2]
      amountValues = allValues[1:25:2]
      req1 = float(countValues[month-1].rstrip('%'))
      req2 = float(amountValues[month-1].rstrip('%'))
      name = df.iloc[i,0:1].values[0]     
      name = name.lstrip('0')
      name = name.title()
      if name == "Jammu And Kashmir":
      	name = "Jammu and Kashmir"
      elif name == "Dadra And Nagar Haveli":
      	name = "Dadra and Nagar Haveli"
      elif name == "Andaman And Nicobar Islands":
      	name = "Andaman and Nicobar Islands"
      elif name == "Daman And Diu":
      	name = "Daman and Diu"
      else:
      	pass
      avgDict[name] = [req1,req2]

    else:
      allValues = df.iloc[i,73:83]
      allValues = list(allValues)
      countValues = allValues[0:25:2]
      amountValues = allValues[1:25:2]
      req1 = float(countValues[month-1].rstrip('%'))
      req2 = float(amountValues[month-1].rstrip('%'))
      name = df.iloc[i,0:1].values[0]     
      name = name.lstrip('0')
      name = name.title()
      if name == "Jammu And Kashmir":
      	name = "Jammu and Kashmir"
      elif name == "Dadra And Nagar Haveli":
      	name = "Dadra and Nagar Haveli"
      elif name == "Andaman And Nicobar Islands":
      	name = "Andaman and Nicobar Islands"
      elif name == "Daman And Diu":
      	name = "Daman and Diu"
      else:
      	pass
      avgDict[name] = [req1,req2]

  return avgDict


def visualize(request):
	if request.method == 'POST':
		form = filterData(request.POST)
		if form.is_valid():
			payment = form.cleaned_data['payment'] 
			year = form.cleaned_data['year']
			month = form.cleaned_data['month']

			monthDict = {'January':1,'February':2,'March':3,'April': 4,'May': 5,'June':6,
			'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

			monthIndex = monthDict[month]


			if payment == 'UPI':
				df1= pd.read_csv("C:/Users/kapil/Desktop/IDRBT/payments/paymentTypes/NPCIData-UPI.csv",header=None)
				upiDetails = getUPINFSPOSDetails(df1,int(year),monthIndex)
				print(upiDetails)
				mp1upi = mapData(upiDetails,"c")
				mp2upi = mapData(upiDetails,"a")
				if int(year)==2017:
					fusionMap1 = makeFusionMap(mp1upi,"1","UPI","c",df1,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2upi,"1","UPI","a",df1,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'1','payment':'upi'
					})



				elif int(year)==2018:
					fusionMap1 = makeFusionMap(mp1upi,"2","UPI","c",df1,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2upi,"2","UPI","a",df1,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'2','payment':'upi'
					})


				elif int(year)==2019:
					fusionMap1 = makeFusionMap(mp1upi,"3","UPI","c",df1,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2upi,"3","UPI","a",df1,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'3','payment':'upi'
					})

				else:
					fusionMap1 = makeFusionMap(mp1upi,"4","UPI","c",df1,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2upi,"4","UPI","a",df1,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'4','payment':'upi'
					})


			elif payment == 'NFS':
				df2= pd.read_csv("C:/Users/kapil/Desktop/IDRBT/payments/paymentTypes/NPCIData-NFS.csv",header=None)
				nfsDetails = getUPINFSPOSDetails(df2,int(year),monthIndex)
				mp1nfs = mapData(nfsDetails,"c")
				mp2nfs = mapData(nfsDetails,"a")
				if int(year)==2017:
					fusionMap1 = makeFusionMap(mp1nfs,"1","NFS","c",df2,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2nfs,"1","NFS","a",df2,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'1','payment':'nfs'
					})

				elif int(year)==2018:
					fusionMap1 = makeFusionMap(mp1nfs,"2","NFS","c",df2,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2nfs,"2","NFS","a",df2,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'2','payment':'nfs'
					})

				elif int(year)==2019:
					fusionMap1 = makeFusionMap(mp1nfs,"3","NFS","c",df2,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2nfs,"3","NFS","a",df2,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'3','payment':'nfs'
					})

				else:
					fusionMap1 = makeFusionMap(mp1nfs,"4","NFS","c",df2,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2nfs,"4","NFS","a",df2,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'4','payment':'nfs'
					})

			elif payment == 'POS':
				df3= pd.read_csv("C:/Users/kapil/Desktop/IDRBT/payments/paymentTypes/NPCIData-POS.csv",header=None)
				posDetails = getUPINFSPOSDetails(df3,int(year),monthIndex)
				mp1pos = mapData(posDetails,"c")
				mp2pos = mapData(posDetails,"a")
				if int(year)==2017:
					fusionMap1 = makeFusionMap(mp1pos,"1","POS","c",df3,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2pos,"1","POS","a",df3,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'1','payment':'pos'
					})

				elif int(year)==2018:
					fusionMap1 = makeFusionMap(mp1pos,"2","POS","c",df3,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2pos,"2","POS","a",df3,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'2','payment':'pos'
					})

				elif int(year)==2019:
					fusionMap1 = makeFusionMap(mp1pos,"3","POS","c",df3,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2pos,"3","POS","a",df3,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'3','payment':'pos'
					})

				else:
					fusionMap1 = makeFusionMap(mp1pos,"4","POS","c",df3,int(year),monthIndex)
					fusionMap2 = makeFusionMap(mp2pos,"4","POS","a",df3,int(year),monthIndex)

					return render(request,'visualize.html',{'output1': fusionMap1.render()
						,'output2': fusionMap2.render(),'form':form,'yeartag':'4','payment':'pos'
					})


			elif payment == "NETC-VAL":
				df4= pd.read_csv("C:/Users/kapil/Desktop/IDRBT/payments/paymentTypes/NPCIData-NETC-Val.csv")
				netcvalDetails = getNETCDetails(df4,int(year),monthIndex)
				mp1netcval = createMapData(netcvalDetails)
				if int(year) == 2017:
					fusionMap3 = createFusionMap(mp1netcval,"1","Val",df4,int(year),monthIndex)
					return render(request,'visualize.html',{'output3': fusionMap3.render(),'form':form,
						'yeartag':'1','payment':'netcval'})
				elif int(year) == 2018:
					fusionMap3 = createFusionMap(mp1netcval,"2","Val",df4,int(year),monthIndex)
					return render(request,'visualize.html',{'output3': fusionMap3.render(),'form':form,
						'yeartag':'2','payment':'netcval'})

				elif int(year) == 2019:
					fusionMap3 = createFusionMap(mp1netcval,"3","Val",df4,int(year),monthIndex)
					return render(request,'visualize.html',{'output3': fusionMap3.render(),'form':form,
						'yeartag':'3','payment':'netcval'})
				elif int(year) == 2020:
					fusionMap3 = createFusionMap(mp1netcval,"4","Val",df4,int(year),monthIndex)
					return render(request,'visualize.html',{'output3': fusionMap3.render(),'form':form,
						'yeartag':'4','payment':'netcval'})
				else:
					pass

			else:
				df5= pd.read_csv("C:/Users/kapil/Desktop/IDRBT/payments/paymentTypes/NPCIData-NETC-Vol.csv")
				netcvolDetails = getNETCDetails(df5,int(year),monthIndex)
				mp1netcvol = createMapData(netcvolDetails)
				if int(year) == 2017:
					fusionMap4 = createFusionMap(mp1netcvol,"1","Vol",df5,int(year),monthIndex)
					return render(request,'visualize.html',{'output4': fusionMap4.render(),'form':form,
						'yeartag':'1','payment':'netcvol'})
				elif int(year) == 2018:
					fusionMap4 = createFusionMap(mp1netcvol,"2","Vol",df5,int(year),monthIndex)
					return render(request,'visualize.html',{'output4': fusionMap4.render(),'form':form,
						'yeartag':'2','payment':'netcvol'})
				elif int(year) == 2019:
					fusionMap4 = createFusionMap(mp1netcvol,"3","Vol",df5,int(year),monthIndex)
					return render(request,'visualize.html',{'output4': fusionMap4.render(),'form':form,
						'yeartag':'3','payment':'netcvol'})
				elif int(year)==2020:
					fusionMap4 = createFusionMap(mp1netcvol,"4","Vol",df5,int(year),monthIndex)
					return render(request,'visualize.html',{'output4': fusionMap4.render(),'form':form,
						'yeartag':'4','payment':'netcvol'})
				else:
					pass

	else:
		form = filterData() 
	return render(request,'visualize.html',{'form':form})


def createMapData(av):

	codeState = {
		'Andaman and Nicobar Islands': ['AN','001'],
		'Andhra Pradesh': ['AP','002'],
		'Arunachal Pradesh': ['AR','003'],
		'Assam': ['AS','004'],
		'Bihar': ['BI','005'],
		'Chandigarh': ['CH','006'],
		'Chhattisgarh': ['CA','007'],
		'Dadra and Nagar Haveli': ['DN','008'],
		'Daman and Diu': ['DD','009'],
		'Delhi': ['DE','010'],
		'Goa': ['GO','011'],
		'Gujarat': ['GU','012'],
		'Haryana': ['HA','013'],
		'Himachal Pradesh': ['HP','014'],
		'Jammu and Kashmir': ['JK','015'],
		'Jharkhand': ['JH','016'],
		'Karnataka': ['KA','017'],
		'Kerala': ['KE','018'],
		'Lakshadweep': ['LA','019'],
		'Madhya Pradesh': ['MP','020'],
		'Maharashtra': ['MA','021'],
		'Manipur': ['MN','022'],
		'Meghalaya': ['ME','023'],
		'Mizoram': ['MI','024'],
		'Nagaland': ['NA','025'],
		'Odisha': ['OR','026'],
		'Puducherry': ['PO','027'],
		'Punjab': ['PU','028'],
		'Rajasthan': ['RA','029'],
		'Sikkim': ['SI','030'],
		'Tamil Nadu': ['TN','031'],
		'Telangana': ['TL','036'],
		'Tripura': ['TR','032'],
		'Uttar Pradesh': ['UP','033'],
		'Uttarakhand': ['UT','034'],
		'West Bengal': ['WB','035']
	}
	mapData = []


	for recStateKey in codeState:

	 	state = recStateKey
	 	stateabb = codeState[state][0]
	 	stateno = codeState[state][1]
	 	lst = []
	 	if (state in av.keys()):
	 		
	 		lst.append(stateabb)
	 		lst.append(av[state])
	 		lst.append(stateno)
	 	else:
	 		lst.append(stateabb)
	 		lst.append(0.00)
	 		lst.append(stateno)


	 	mapData.append(lst)
    
	return mapData

def createFusionMap(mpdata,tag,tag2,df,year,month):

	dataSource = OrderedDict()

	# The `mapConfig` dict contains key - value pairs data for chart attribute
	mapConfig = OrderedDict()
	if tag == "1":
		if tag2 == "Val":
			mapConfig["caption"] = "Average NETC Val Payments Statewise in 2017"
		else:
			mapConfig["caption"] = "Average NETC Vol Payments Statewise in 2017"

	elif tag == "2":
		if tag2 == "Val":
			mapConfig["caption"] = "Average NETC Val Payments Statewise in 2018"
		else:
			mapConfig["caption"] = "Average NETC Vol Payments Statewise in 2018"

	elif tag == "3":
		if tag2 == "Val":
			mapConfig["caption"] = "Average NETC Val Payments Statewise in 2019"
		else:
			mapConfig["caption"] = "Average NETC Vol Payments Statewise in 2019"
	else:
		if tag2 == "Val":
			mapConfig["caption"] = "Average NETC Val Payments Statewise in 2020"
		else:
			mapConfig["caption"] = "Average NETC Vol Payments Statewise in 2020"

	na = getNETCNationalAverage(df,year,month)

	r1 = na - (0.2*na)

	r2 = na + (0.1*na)


	mapConfig["includevalueinlabels"] = "1"
	mapConfig["numbersuffix"] = "%"
	mapConfig["labelsepchar"] = ":"
	mapConfig["entityFillHoverColor"] = "#FFF9C4"
	mapConfig["theme"] = "fusion"

	# Map color range data
	colorDataObj = {
		"minvalue": "0",
		"code": "#FFE0B2",
		"gradient": "1",
		"color": [{
				"minValue": "0.00",
				"maxValue": str(r1),
				"code": "#E65100"
			},
			{
				"minValue": str(r1),
				"maxValue": str(r2),
				"code": "#FFBF00 "
			},
			{
				"minValue": str(r2),
				"maxValue": "27.00",
				"code": "#228B22"
			}
		]
	}

	dataSource["chart"] = mapConfig
	dataSource["colorrange"] = colorDataObj
	dataSource["data"] = []


	mapDataArray = mpdata


	for i in range(len(mapDataArray)):
		dataSource["data"].append({
			"id": mapDataArray[i][2],
			"value": mapDataArray[i][1],
			"showLabel": mapDataArray[i][0]
		})




	fusionMap = FusionCharts("maps/india", "myFirstMap-"+tag+tag2, "800", "800", "myFirstchart-container-"+tag+tag2, "json", dataSource)

	return fusionMap

def makeFusionMap(mpdata,tag,tag2,tag3,df,year,month):

	dataSource = OrderedDict()
	mapConfig = OrderedDict()
	if tag == "1":
		if tag2 == "UPI":
			if tag3 == "c":
				mapConfig["caption"] = "Average UPI Payments Statewise in 2017 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average UPI Payments Statewise in 2017 (Average Amount Percentages)"

		elif tag2 == "NFS":
			if tag3 == "c":
				mapConfig["caption"] = "Average NFS Payments Statewise in 2017 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average NFS Payments Statewise in 2017 (Average Amount Percentages)"

		else:
			if tag3 == "c":
				mapConfig["caption"] = "Average POS Payments Statewise in 2017 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average POS Payments Statewise in 2017 (Average Amount Percentages)"

	elif tag == "2":
		if tag2 == "UPI":
			if tag3 == "c":
				mapConfig["caption"] = "Average UPI Payments Statewise in 2018 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average UPI Payments Statewise in 2018 (Average Amount Percentages)"

		elif tag2 == "NFS":
			if tag3 == "c":
				mapConfig["caption"] = "Average NFS Payments Statewise in 2018 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average NFS Payments Statewise in 2018 (Average Amount Percentages)"

		else:
			if tag3 == "c":
				mapConfig["caption"] = "Average POS Payments Statewise in 2018 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average POS Payments Statewise in 2018 (Average Amount Percentages)"

	elif tag == "3":
		if tag2 == "UPI":
			if tag3 == "c":
				mapConfig["caption"] = "Average UPI Payments Statewise in 2019 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average UPI Payments Statewise in 2019 (Average Amount Percentages)"

		elif tag2 == "NFS":
			if tag3 == "c":
				mapConfig["caption"] = "Average NFS Payments Statewise in 2019 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average NFS Payments Statewise in 2019 (Average Amount Percentages)"

		else:
			if tag3 == "c":
				mapConfig["caption"] = "Average POS Payments Statewise in 2019 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average POS Payments Statewise in 2019 (Average Amount Percentages)"
	else:
		if tag2 == "UPI":
			if tag3 == "c":
				mapConfig["caption"] = "Average UPI Payments Statewise in 2020 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average UPI Payments Statewise in 2020 (Average Amount Percentages)"

		elif tag2 == "NFS":
			if tag3 == "c":
				mapConfig["caption"] = "Average NFS Payments Statewise in 2020 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average NFS Payments Statewise in 2020 (Average Amount Percentages)"

		else:
			if tag3 == "c":
				mapConfig["caption"] = "Average POS Payments Statewise in 2020 (Average Count Percentages)"
			else:
				mapConfig["caption"] = "Average POS Payments Statewise in 2020 (Average Amount Percentages)"

	na = getUPINFSPOSNationalAverage(df,year,month)

	r1 = na - (0.2*na)

	r2 = na + (0.1*na)


	mapConfig["includevalueinlabels"] = "1"
	mapConfig["numbersuffix"] = "%"
	mapConfig["labelsepchar"] = ":"
	mapConfig["entityFillHoverColor"] = "#FFF9C4"
	mapConfig["theme"] = "fusion"

	# Map color range data
	colorDataObj = {
		"minvalue": "0",
		"code": "#FFE0B2",
		"gradient": "1",
		"color": [{
				"minValue": "0.00",
				"maxValue": str(r1),
				"code": "#E65100"
			},
			{
				"minValue": str(r1),
				"maxValue": str(r2),
				"code": "#FFBF00 "
			},
			{
				"minValue": str(r2),
				"maxValue": "27.00",
				"code": "#228B22"
			}
		]
	}

	dataSource["chart"] = mapConfig
	dataSource["colorrange"] = colorDataObj
	dataSource["data"] = []


	mapDataArray = mpdata


	for i in range(len(mapDataArray)):
		dataSource["data"].append({
			"id": mapDataArray[i][2],
			"value": mapDataArray[i][1],
			"showLabel": mapDataArray[i][0]
		})



	fusionMap = FusionCharts("maps/india", "myFirstMap-"+tag+tag2+tag3, "800", "800", "myFirstchart-container-"+tag+tag2+tag3, "json", dataSource)

	return fusionMap

def mapData(av,tag):
	codeState = {
		'Andaman and Nicobar Islands': ['AN','001'],
		'Andhra Pradesh': ['AP','002'],
		'Arunachal Pradesh': ['AR','003'],
		'Assam': ['AS','004'],
		'Bihar': ['BI','005'],
		'Chandigarh': ['CH','006'],
		'Chhattisgarh': ['CA','007'],
		'Dadra and Nagar Haveli': ['DN','008'],
		'Daman and Diu': ['DD','009'],
		'Delhi': ['DE','010'],
		'Goa': ['GO','011'],
		'Gujarat': ['GU','012'],
		'Haryana': ['HA','013'],
		'Himachal Pradesh': ['HP','014'],
		'Jammu and Kashmir': ['JK','015'],
		'Jharkhand': ['JH','016'],
		'Karnataka': ['KA','017'],
		'Kerala': ['KE','018'],
		'Lakshadweep': ['LA','019'],
		'Madhya Pradesh': ['MP','020'],
		'Maharashtra': ['MA','021'],
		'Manipur': ['MN','022'],
		'Meghalaya': ['ME','023'],
		'Mizoram': ['MI','024'],
		'Nagaland': ['NA','025'],
		'Odisha': ['OR','026'],
		'Puducherry': ['PO','027'],
		'Punjab': ['PU','028'],
		'Rajasthan': ['RA','029'],
		'Sikkim': ['SI','030'],
		'Tamil Nadu': ['TN','031'],
		'Telangana': ['TL','036'],
		'Tripura': ['TR','032'],
		'Uttar Pradesh': ['UP','033'],
		'Uttarakhand': ['UT','034'],
		'West Bengal': ['WB','035']
	}
	mapData = []


	for recStateKey in codeState:

	 	state = recStateKey
	 	stateabb = codeState[state][0]
	 	stateno = codeState[state][1]
	 	lst = []
	 	if (state in av.keys()):
	 		
	 		lst.append(stateabb)
	 		if tag == "c":
	 			lst.append(av[state][0])
	 		else:
	 			lst.append(av[state][1])

	 		lst.append(stateno)
	 	else:
	 		lst.append(stateabb)
	 		lst.append(0.00)
	 		lst.append(stateno)


	 	mapData.append(lst)
    
	return mapData
