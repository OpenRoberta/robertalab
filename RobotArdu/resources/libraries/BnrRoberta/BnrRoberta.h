/*
  BnrRoberta.cpp - additional library for interfacing with Bot'n Roll ONE Arduino Compatible 
  from www.botnroll.com that allows using some extra functions from https://www.open-roberta.org/
  Created by Evgeniya Ovchinnikova, August 30, 2016.
  Released into the public domain.
*/

#ifndef BnrRoberta_h
#define BnrRoberta_h

#include <stdio.h>
#include <stdlib.h>
#include<stdio.h>
#include<string.h>
#include "Arduino.h"
#include "BnrOneA.h" 
#include "BnrRescue.h" 
#include "Wire.h" 


class BnrRoberta
{
  public:   
		void moveTime(int speedL,int speedR, double time);
		void moveTimePID(int speedL,int speedR, double time);
		void move1mTime(int port, int speed, double time);
		void lcdClear();
		int ultrasonicDistance(int port);
		int sonar();
		bool buttonIsPressed(int button);
		byte *colorSensorRGB(byte colors[],int port);
		int colorSensorLight(byte colors[], int port);
		String colorSensorColor(byte colors[], int port);
		bool infraredSensorObstacle(int port);
		bool infraredSensorPresence(int port);
		float readBearing();
		char readRoll();
		char readPitch();
		BnrRoberta(BnrOneA one, BnrRescue brm);
		BnrOneA one;
		BnrRescue brm;
		void setOne(BnrOneA oneInn);
		void setBrm(BnrRescue brmInn);
		void dtoa(double n, char *res, int afterpoint);
		int intToStr(int x, char str[], int d);
		void reverse(char *str, int len);
		char *numToString(double num);
		char *boolToString(bool boolean);
};
#endif

