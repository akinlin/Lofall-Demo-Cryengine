#include "TimeManager.h"

CTimeManager::CTimeManager()
{
	Hours = 0;
	Minutes = 0;
	Seconds = 0;
}

CTimeManager::~CTimeManager() {}

const char* CTimeManager::getCurrentTime()
{
	//gEnv->p3DEngine->GetTimeOfDay();
	char* result = "--:--:--"; 
	sprintf(result, "%d%s%d%s%d", Hours, ":", Minutes, ":", Seconds);
	return result;
}