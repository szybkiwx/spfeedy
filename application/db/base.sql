CREATE TABLE User (
id integer primary key autoincrement,
username text,
password text,
salt text	
);

CREATE TABLE Category (
id integer primary key autoincrement,
name text, 
parentid integer, 
userid integer,
foreign key(parentid) references Category(id),
foreign key(userid) references User(id)
);

CREATE TABLE Subscription (
id integer primary key autoincrement,
title text,
url text,
categoryid integer,
foreign key(categoryid) references Category(id)
);

create table Feed (
id integer primary key autoincrement, 
title text,
link text,
description text,
subscriptionid integer, 
foreign key(subscriptionid) references Subscription(id)
);
