/**
* \par Fraunhofer  IAIS, OpenRoberta project, 2017
* \class MeDrive
* \brief   Support for differential drive and wrapper around MeDCMotor
* @file    MeDrive.cpp
* @author  Artem Vinokurov
* @version V1.0.0
* @date    2017/05/08
* @brief   MeDrive.cpp module implementation
*
*
* \par Copyright
* This software is Copyright (C), 2012-2016, MakeBlock. Use is subject to license \n
* conditions. The main licensing options available are GPL V2 or Commercial: \n
*
* \par Open Source Licensing GPL V2
* This is the appropriate option if you want to share the source code of your \n
* application with everyone you distribute it to, and you also want to give them \n
* the right to share who uses it. If you wish to use this software under Open \n
* Source Licensing, you must contribute all your source code to the open source \n
* community in accordance with the GPL Version 2 when your application is \n
* distributed. See http://www.gnu.org/copyleft/gpl.html
*
*
* \par Method List:
*
*    1. void MeDrive::drive(uint8_t speed, boolean direction)
*
* \par History:
* <pre>
* `<Author>`         `<Time>`        `<Version>`        `<Descr>`
* Artem Vinokurov         2017/05/08     1.0.0            Initial method for run
* </pre>
*
*/

#include "MeDrive.h"

MeDrive::MeDrive() : leftMotor(M2), rigthMotor(M1)
{
}

MeDrive::MeDrive(uint8_t leftMotorPort, uint8_t rightMotorPort) : leftMotor(leftMotorPort), rigthMotor(rightMotorPort)
{
}

MeDrive::~MeDrive()
{
}

void MeDrive::drive(int16_t speed, boolean direction)
{
    steer(speed, speed, direction);
}

void MeDrive::drive(int16_t speed, boolean direction, uint16_t duration)
{
    steer(speed, speed, direction, duration);
}

void MeDrive::turn(int16_t speed, boolean direction)
{
	turn(speed, direction, 0);
}

void MeDrive::turn(int16_t speed, boolean direction, uint16_t duration)
{
	if (direction)
	{
		// left
		steer(speed, -1*speed, 0, duration);
	}
	else
	{
		// right
		steer(-1*speed, speed, 0, duration);
	}
}

void MeDrive::steer(int16_t speedLeft, int16_t speedRight, boolean direction)
{
	// duration 0 means infinite steer (drive)
	steer(speedLeft, speedRight, direction, 0);
}

void MeDrive::steer(int16_t speedLeft, int16_t speedRight, boolean direction, uint16_t duration)
{
	/* 
	* speed is given in percentage
    * max speed is 255, so we double the given speed
	* also: true or 1 is forward
    */
	if (direction) 
	{
		leftMotor.run(-2*speedLeft);
        rigthMotor.run(2*speedRight);
	}
	else
    {
        leftMotor.run(2*speedLeft);
        rigthMotor.run(-2*speedRight);
    }
	if (duration != 0) {
		delay(duration);
		leftMotor.stop();
		rigthMotor.stop();
	}
}

void MeDrive::stop()
{
	leftMotor.stop();
	rigthMotor.stop();
}