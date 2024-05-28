select * from sys.tables

create table custData(
						id int primary key,
						EName varchar(3),
						Age int,
						pinCode int,
						Cities varchar(13),
						salary int,
						RepMgrID int)

select * from custData