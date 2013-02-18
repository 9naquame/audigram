function Pound()
{
	var temp = parseFloat(document.currencyForm.pounnd.value)
	temp = twoDecPlace(temp);
	if (isNaN(temp) || temp<0)
	{
		temp=0;
	}
	
	
	dollar = twoDecPlace(temp/1.5671);
	euro = twoDecPlace(temp*1.19997);
	cedi = twoDecPlace(temp*2.70);
	
	document.currencyForm.dollar.value = dollar;
	document.currencyForm.euro.value = euro;
	document.currencyForm.cedi.value = cedi;
}


function Dollar()
{
	var temp = parseFloat(document.currencyForm.dollar.value)
	temp = twoDecPlace(temp);
	
	if (isNaN(temp) || temp<0)
	{
		temp=0;
	}
	
	cedi = twoDecPlace(temp*1.7269);
	pounnd = twoDecPlace(temp*1.5671);
	euro = twoDecPlace(temp*1.3409);
	
	
	document.currencyForm.pounnd.value  = pounnd;
	document.currencyForm.euro.value = euro;
	document.currencyForm.cedi.value = cedi;
}

function Euro()
{
	var temp = parseFloat(document.currencyForm.euro.value)
	temp = twoDecPlace(temp);
	if (isNaN(temp) || temp<0)
	{
		temp=0;
	}
	dollar = twoDecPlace(temp/1.3409);
	pounnd = twoDecPlace(temp/1.19997);
	cedi = twoDecPlace(temp*2.24);
	
	document.currencyForm.dollar.value  = dollar;
	document.currencyForm.pounnd.value = pounnd;
	document.currencyForm.cedi.value = cedi;
}


function Cedi()
{
	var temp = parseFloat(document.currencyForm.cedi.value)
	temp = twoDecPlace(temp);
	if (isNaN(temp) || temp<0)
	{
		temp=0;
	}
	
	dollar = twoDecPlace(temp/1.7269);
	pounnd = twoDecPlace(temp/2.70);
	euro = twoDecPlace(temp/2.24);
	
	document.currencyForm.dollar.value  = dollar;
	document.currencyForm.pounnd.value = pounnd;
	document.currencyForm.euro.value = euro;
}


function twoDecPlace(num) 
{
	return Math.round(num * 100) / 100;
}
