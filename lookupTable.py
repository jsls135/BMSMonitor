CellTempADRaw= (409, 561, 779, 1091, 1567, 1863, 2216,2637,
				3136, 3724, 4410, 5201, 6116, 7083, 8088, 9114,
				10139, 11138,12080, 12935, 13680, 14299, 14788)

CellTempValue= (100,90,80,70,60,55,50,45,
				40,35,30,25,20,15,10,5,
				0,-5,-10,-15,-20,-25,-30)
				
def lookupTable(inputAdValue):
	global CellTempADRaw,CellTempValue
	if inputAdValue <= 409:
		returnValue=100            
	elif inputAdValue > 14788:
		returnValue=-30
	else:
		for item in range(1,23):
			if inputAdValue <= CellTempADRaw[item]:
				returnValue=((CellTempADRaw[item]-inputAdValue)*(CellTempValue[item-1]-CellTempValue[item]))/(CellTempADRaw[item]-CellTempADRaw[item-1])+CellTempValue[item]
				break
	return returnValue
		
#if __name__ == "__main__":
#	#main(sys.argv)
#	test=lookupTable(450)
#	print "value:",str(test)