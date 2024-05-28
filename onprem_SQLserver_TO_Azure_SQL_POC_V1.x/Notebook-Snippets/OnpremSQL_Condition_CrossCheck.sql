select * from sys.tables

select * from tblemps
select * from tblCity

insert into tblemps(id,EName ,Age,AreaPinCode,salary) values (10,'HHH',20,700083,15500)
insert into tblCity(pinCode,city) values (50,'INVALID CITY')

select id,EName ,Age,AreaPinCode,city,salary,RepMgrID from tblemps e
left join tblCity c
on e.AreaPinCode = c.pinCode