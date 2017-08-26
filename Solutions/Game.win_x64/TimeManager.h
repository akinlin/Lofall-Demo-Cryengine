#pragma once

#include "StdAfx.h"

class CTimeManager
{
public:
	CTimeManager();
	virtual ~CTimeManager();

	// returns a time format HH:MM:SS
	const char* getCurrentTime();

	bool is24Hour() { return Is24HourTime; };
	void set24Hour(bool is24HourOn) { Is24HourTime = is24HourOn; };

private:

	bool Is24HourTime = false;
	int Hours;
	int Minutes;
	int Seconds;
};