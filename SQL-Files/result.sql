SELECT email,
sum(
case 
	when fixedamount = True 
	then donation
	else 0
end ), count(case 
	when fixedamount = True 
	then 1
	else 0
end),
sum(
case 
	when fixedamount = False 
	then donation
	else 0
end ), count(case 
	when fixedamount = False
	then 1
	else 0
end)
	FROM public.api_donationrecord
	group by email;





