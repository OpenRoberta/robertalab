/*
  RobertaFunctions.cpp - additional library for interfacing with Bot'n Roll ONE Arduino Compatible 
  from www.botnroll.com that allows using some extra functions from https://www.open-roberta.org/
  Created by Evgeniya Ovchinnikova, August 30, 2016.
  Released into the public domain.
*/

#ifndef RobertaFunctions_h
#define RobertaFunctions_h

#include <stdio.h>
#include <stdlib.h>
#include<stdio.h>
#include<string.h>
#include "Arduino.h"


class RobertaFunctions
{
  public:   
		int randomIntegerInRange(int val1, int val2);
		float randomFloat();
		double clamp(double val, double min, double max);
		bool isPrime(double number);
		bool isWhole(double val);
		int arrFindFirst(int len, double arr[], double item);
		int arrFindFirst(int len, bool arr[], bool item);
		int arrFindFirst(int len, String arr[], String item);
		int arrFindLast(int len, double arr[], double item);
		int arrFindLast(int len, bool arr[], bool item);
		int arrFindLast(int len, String arr[], String item);
		double arrSum(int len, double arr[]);
		double arrMin(int len, double arr[]);
		double arrMax(int len, double arr[]);
		double arrMean(int len, double arr[]);
		void arrInsertionSort(int len,  double *arr);
		double arrMedian(int len, double arr[]);
		double arrStandardDeviatioin(int len, double arr[]);
		double arrRand(int len, double arr[]);
		double arrMode(int len, double arr[]);
};
#endif

