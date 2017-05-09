/**
* \par Fraunhofer  IAIS, OpenRoberta project, 2017
* \class MeDrive
* \brief   Support for differential drive and wrapper around MeDCMotor
* @file    MeDrive.h
* @author  Artem Vinokurov
* @version V1.0.0
* @date    2017/05/08
* @brief   Header for MeDrive.cpp module
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

#ifndef MeDrive_H
#define MeDrive_H

#include "MeDCMotor.h"

class MeDrive
{
public:
    /* true for forward, false for backward drive direction */
    void drive(int16_t speed, boolean direction);
	void drive(int16_t speed, boolean direction, uint16_t duration);
	void turn(int16_t speed, boolean direction);
	void turn(int16_t speed, boolean direction, uint16_t duration);
	void steer(int16_t speedLeft, int16_t speedRight, boolean direction);
	void steer(int16_t speedLeft, int16_t speedRight, boolean direction, uint16_t duration);
	void stop();
    /* constructor - destructor pair */
    MeDrive();
    MeDrive(uint8_t leftMotorPort, uint8_t rightMotorPort);
    ~MeDrive();
private:
    MeDCMotor leftMotor;
    MeDCMotor rigthMotor;
};
#endif /* MeDrive_H */
