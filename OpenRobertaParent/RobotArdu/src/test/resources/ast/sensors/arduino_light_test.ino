// This file is automatically generated by the Open Roberta Lab.

#include <math.h>
#include <RobertaFunctions.h>   // Open Roberta library
#include <NEPODefs.h>

RobertaFunctions rob;

double item;
int _output_L = A0;
void setup()
{
    Serial.begin(9600); 
    item = analogRead(_output_L)/10.24;
}

void loop()
{
}