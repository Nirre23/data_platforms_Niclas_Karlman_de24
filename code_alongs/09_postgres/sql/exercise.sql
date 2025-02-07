-- select count(utbildningsnamn)as total_DataEngineers,
-- "utbildningsanordnare administrativ enhet"
-- from 
--     myh_2024
-- where 
--     utbildningsområde = 'Data/IT'
-- and 
--     utbildningsnamn = 'Data Engineer'
-- group by "utbildningsanordnare administrativ enhet";

-- select count(utbildningsnamn) as total_DataEngineers, beslut, "län"
-- from myh_2024
-- where utbildningsnamn = 'Data Engineer'
-- and beslut = 'Beviljad' 
-- group by beslut , "län"

-- SELECT count("sun5 inriktning namn") total ,utbildningsområde,  kommun, beslut
-- from myh_2024
-- where beslut = 'Beviljad'
-- group by  kommun, "utbildningsområde","sun5 inriktning namn",beslut

-- SELECT count(utbildningsnamn) as approved, kommun
-- FROM myh_2024
-- WHERE beslut = 'Beviljad'
-- GROUP BY kommun
-- order by approved desc;

-- select utbildningsnamn, "antal kommuner"
-- from myh_2024
-- where beslut = 'Beviljad' and "antal kommuner" > 1

-- select utbildningsnamn ,"sun5 inriktning namn", beslut, count(*)
-- from myh_2024 
-- where beslut = 'Beviljad'
-- group by utbildningsnamn,"sun5 inriktning namn",beslut
-- order by utbildningsnamn asc;

-- select utbildningsnamn, beslut,län
-- from myh_2024 
-- where län = 'Stockholm' and beslut = 'Beviljad'

-- select utbildningsnamn,"yh-poäng", beslut
-- from myh_2024
-- where beslut = 'Beviljad' and "yh-poäng" = 400;

-- select utbildningsnamn, beslut
-- from myh_2024 
-- where beslut != 'Beviljad'
-- order by utbildningsnamn asc;

-- select utbildningsnamn, "typ av examen", beslut
-- from myh_2024
-- where "typ av examen" = 'Yrkeshögskoleexamen' and beslut = 'Beviljad' limit 10;

-- select count(utbildningsnamn) as total_DataEngineers, "utbildningsanordnare administrativ enhet"
-- from 
--     myh_2024
-- where utbildningsnamn = 'Data Engineer'    
-- group by "utbildningsanordnare administrativ enhet"

SELECT count(utbildningsnamn) as "Data Engineers",beslut,"utbildningsanordnare administrativ enhet"
from
myh_2024
where beslut = 'Beviljad'
group by utbildningsnamn, beslut,"utbildningsanordnare administrativ enhet"
