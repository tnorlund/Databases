#!/usr/bin/python3

import cgi, os
import cgitb
import pymysql

def check_and_init_tables(cursor, connection):
  db_init = True; 
  cursor.execute("SHOW TABLES;")
  tables = cursor.fetchall();
  orig_tables = ["Application", "Media", "Essay", "Show", "Medical", 
    "Job"]
  print(f"tables:{tables}")  

  if (tables == orig_tables):
    db_init = False;
    cursor.execute("CREATE TABLE Application (" + 
      "ApplicationID      INT UNSIGNED NOT NULL, " + 
      "Name               VARCHAR(50), " + 
      "Address_City       VARCHAR(50), " + 
      "Address_State      VARCHAR(2), " + 
      "Address_PostalCode SMALLINT UNSIGNED, " + 
      "Phone_Day          VARCHAR(20), " + 
      "Phone_Night        VARCHAR(20), " + 
      "Email              VARCHAR(50), " + 
      "DOB                DATE, " + 
      "Gender             ENUM ('M', 'F'), " +
      "MediaID            INT, " +
      "EssayID            INT, " +
      "ShowID             INT, " +
      "PRIMARY KEY (ApplicationID), " + 
      "FOREIGN KEY (MediaID)   REFERENCES Media(MediaID), " + 
      "FOREIGN KEY (EssayID)   REFERENCES Essay(EssayID), " + 
      "FOREIGN KEY (ShowID)    REFERENCES Show(ShowID), " + 
      ");");
    cursor.execute("CREATE TABLE Media (" + 
      "MediaID INT NOT NULL, " + 
      "PhotoID INT UNSIGNED, " + 
      "VideoID INT UNSIGNED, " + 
      "PRIMARY KEY (ContestantID), " +
      ");");
    cursor.execute("CREATE TABLE Essay (" + 
      "EssayID  INT UNSIGNED NOT NULL, " + 
      "Path     VARCHAR(50), " + 
      "FileName VARCHAR(50) " + 
      "PRIMARY KEY (EssayID) " + 
      ");");
    cursor.execute("CREATE TABLE Show (" + 
      "ShowID   INT UNSIGNED NOT NULL, " + 
      "Ratings  INT UNSIGNED, " + 
      "Producer INT UNSIGNED, " + 
      "Director INT UNSIGNED, " + 
      "PRIMARY KEY (ShowID) " + 
      ");");
    cursor.execute("CREATE TABLE Medical (" + 
      "ContestantID INT UNSIGNED NOT NULL, " + 
      "Medications  INT UNSIGNED, " + 
      "Reasons INT  VARCHAR(50), " + 
      "FOREIGN KEY (ContestantID) REFERENCES Contestant(ContestantID)" + 
      ");");
    cursor.execute("CREATE TABLE Job (" + 
      "ContestantID INT UNSIGNED NOT NULL, " + 
      "JobName      INT UNSIGNED, " + 
      "StartTime    INT UNSIGNED, " + 
      "EndTime      INT UNSIGNED, " + 
      "Description  INT UNSIGNED, " + 
      "FOREIGN KEY (ContestantID) REFERENCES Contestant(ContestantID)" + 
      ");");
    cursor.execute("CREATE TABLE BackgroundCheck (" + 
      "BackgroundCheckID INT UNSIGNED NOT NULL, " + 
      "ContestantID      INT UNSIGNED, " + 
      "NationalID        VARCHAR(20), " + 
      "Religion          VARCHAR(20), " + 
      "Rating_Appearance SMALLINT UNSIGNED, " + 
      "Rating_Strength   SMALLINT UNSIGNED, " + 
      "PRIMARY KEY (BackgroundCheckID), " + 
      "FOREIGN KEY (ContestantID) REFERENCES Contestant(ContestantID) " + 
      ");");
    cursor.execute("CREATE TABLE Employer (" + 
      "BackgroundCheckID INT UNSIGNED, " + 
      "Name              VARCHAR(50), " + 
      "Phone             VARCHAR(20), " + 
      "Comments          VARCHAR(256), " +  
      "FOREIGN KEY (BackgroundCheckID) REFERENCES BackgroundCheck(BackgroundCheckID) " + 
      ");");
    cursor.execute("CREATE TABLE Education (" + 
      "BackgroundCheckID INT UNSIGNED, " + 
      "Education         VARCHAR(50), " +
      "Phone             VARCHAR(20), " + 
      "Degree            VARCHAR(50), " +
      "Comments          VARCHAR(256), " +  
      "FOREIGN KEY (BackgroundCheckID) REFERENCES BackgroundCheck(BackgroundCheckID) " + 
      ");");
    cursor.execute("CREATE TABLE PoliceRecord (" + 
      "BackgroundCheckID INT UNSIGNED, " + 
      "Date              DATE, " +
      "Category          VARCHAR(20), " + 
      "Description       VARCHAR(256), " + 
      "Outcome           VARCHAR(256), " + 
      "FOREIGN KEY (BackgroundCheckID) REFERENCES BackgroundCheck(BackgroundCheckID) " + 
      ");");
    cursor.execute("CREATE TABLE Event (" + 
      "EventID         INT UNSIGNED, " + 
      "Description     DATE, " +
      "EstimatedTime   VARCHAR(20), " + 
      "EstimatedDanger VARCHAR(256), " + 
      "Producer        VARCHAR(256), " + 
      "Director        VARCHAR(256), " + 
      "Episode         VARCHAR(256), " + 
      "PRIMARY KEY (EventID) " + 
      ");");
    cursor.execute("CREATE TABLE Action (" + 
      "EventID       INT UNSIGNED, " + 
      "Sequence      INT, " +
      "Description   VARCHAR(256), " +  
      "Cameras       INT, " + 
      "EstimatedTime INT, " + 
      "FOREIGN KEY (EventID) REFERENCES Event(EventID) " + 
      ");");
    cursor.execute("CREATE TABLE Contestant (" + 
      "ContestantID INT UNSIGNED, " + 
      "EventID      INT UNSIGNED, " + 
      "Name         VARCHAR(50), , " +
      "Task         VARCHAR(256), " +  
      "Result       VARCHAR(256), " + 
      "Points       INT, " + 
      "Prize        VARCHAR(256), " + 
      "PRIMARY KEY (ContestantID), " + 
      "FOREIGN KEY (EventID) REFERENCES Event(EventID) " + 
      ");");
    cursor.execute("CREATE TABLE Vote (" + 
      "VoteID          INT UNSIGNED, " + 
      "Episode_Title   INT UNSIGNED, " + 
      "Episode_AirDate VARCHAR(50), , " +
      "PRIMARY KEY (VoteID), " + 
      ");");

    connection.commit()
  return db_init;

conn = pymysql.connect(
  db='RelationalDatabasesFinal',
  user='root',
  passwd='',
  host='localhost');
cur = conn.cursor();
if (not check_and_init_tables(cursor=cur, connection=conn)):
  print("Initialized Table");


