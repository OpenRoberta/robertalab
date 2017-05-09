/*
  RobertaFunctions.cpp - additional library for interfacing with Bot'n Roll ONE Arduino Compatible
  from www.botnroll.com that allows using some extra functions from https://www.open-roberta.org/
  Created by Evgeniya Ovchinnikova, August 30, 2016.
  Released into the public domain.
*/
#include <stdio.h>
#include <stdlib.h>
#include "SPI.h"
#include "math.h"
#include "RobertaFunctions.h"


int RobertaFunctions::randomIntegerInRange(int val1, int val2){
	int min = fmin(val1, val2);
	int max = fmax(val1, val2);
	return min + (rand()%(min - max));
}

float RobertaFunctions::randomFloat(){
	return (float)rand()/(float)RAND_MAX;
}

double RobertaFunctions::clamp(double val, double min, double max){
	return fmin(fmax(val, min), max);
}

bool RobertaFunctions::isPrime(double number) {
    if ((fmod(number, 2) == 0) || (number == 1)) return false;
    //if not, then just check the odds
    for(int i = 3; i * i <= number; i += 2) {
        if(fmod(number, i) == 0)
            return false;
    }
    return true;
}

bool RobertaFunctions::isWhole(double val){
  int intPart = val;
  return ((val - intPart) == 0);
}

int RobertaFunctions::arrFindFirst(int len, double arr[], double item) {
  int i = 0;
  if (arr[0] == item){
    return i;
  } else {
    do {
      i++;
    } while((arr[i] != item) && (i != len));
    return i;
  }
}

int RobertaFunctions::arrFindFirst(int len, bool arr[], bool item) {
  int i = 0;
  if (arr[0] == item){
    return i;
  } else {
    do {
      i++;
    } while((arr[i] != item) && (i != len));
    return i;
  }
}

int RobertaFunctions::arrFindFirst(int len, String arr[], String item) {
  int i = 0;
  if (arr[0] == item){
    return i;
  } else {
    do {
      i++;
    } while((arr[i] != item) && (i != len));
    return i;
  }
}


int RobertaFunctions::arrFindLast(int len, double arr[], double item) {
  int i = 0;
  if (arr[len - 1] == item){
    return len - 1 - i;
  } else {
    do {
      i++;
    } while((arr[len - 1 - i] != item)&&(i != 0));
      return len - 1 - i;
  }
}

int RobertaFunctions::arrFindLast(int len, bool arr[], bool item) {
  int i = 0;
  if (arr[len - 1] == item){
    return len - 1 - i;
  } else {
    do {
      i++;
    } while((arr[len - 1 - i] != item)&&(i != 0));
      return len - 1 - i;
  }
}
int RobertaFunctions::arrFindLast(int len, String arr[], String item) {
  int i = 0;
  if (arr[len - 1] == item){
    return len - 1 - i;
  } else {
    do {
      i++;
    } while((arr[len - 1 - i] != item)&&(i != 0));
      return len - 1 - i;
  }
}




double RobertaFunctions::arrSum(int len, double arr[]) {
  float sum = 0;
  for(int i = 0; i < len; i++) {
    sum += arr[i];
  }
  return sum;
}
double RobertaFunctions::arrMin(int len, double arr[]) {
  double min = arr[0];
  for(int i = 1; i < len; i++) {
    if (arr[i] < min){
      min = arr[i];
    }
  }
  return min;
}
double RobertaFunctions::arrMax(int len, double arr[]) {
  double max = arr[0];
  for(int i = 1; i < len; i++) {
    if (arr[i] > max){
      max = arr[i];
    }
  }
  return max;
}
double RobertaFunctions::arrMean(int len, double arr[]) {
  double sum = 0;
  for(int i = 0; i < len; i++) {
    sum += arr[i];
  }
  return sum/len;
}
void RobertaFunctions::arrInsertionSort(int len,  double *arr) {
  for (int i=1; i < len; i++) {
    int index = arr[i];
    int j = i;
    while (j > 0 && arr[j-1] > index) {
      arr[j] = arr[j-1];
      j--;
    }
    arr[j] = index;
  }
}
double RobertaFunctions::arrMedian(int len, double arr[]) {
  if (len == 0) {
    return 0;
  }
  arrInsertionSort(len, arr);
  double median;
  if (len % 2 == 0) {
    median = (arr[len / 2] + arr[len / 2 - 1]) / 2;
  } else {
    median = arr[len / 2];
  }
  return median;
}

double RobertaFunctions::arrStandardDeviatioin(int len, double arr[]) {
  if (len == 0) {
    return 0;
  }
  double variance = 0;
  double mean = arrMean(len, arr);
  for (int i = 0; i < len; i++) {
    variance += pow(arr[i] - mean, 2);
  }
  variance /= len;
  return sqrt(variance);
}

double RobertaFunctions::arrRand(int len, double arr[]) {
  int arrayInd = len * (randomFloat()*100)/100;
  return arr[arrayInd - 1];
}

double RobertaFunctions::arrMode(int len, double arr[]){
  arrInsertionSort(len, arr);
  double element = arr[0];
  double max_seen = element;
  int count = 1;
  int mode_count = 1;
  for (int i = 1; i < len; i++){
    if (arr[i] == element){
      count++;
      if (count > mode_count) {
        mode_count = count;
        max_seen = element;
      }
    } else {
      element = arr[i];
      count = 1;
    }
  }
  return max_seen;
}
