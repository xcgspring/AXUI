// screenshot.cpp : screen capture.
// code from http://msdn.microsoft.com/en-us/library/dd183402(v=vs.85).aspx

#include "stdafx.h"
#include <Windows.h>
#include <stdlib.h>
#include "wingetopt.h"

int CaptureAnImage(HWND hWnd, RECT rcClient, char* filename)
{
	HDC hdcScreen;
	HDC hdcWindow;
	HDC hdcMemDC = NULL;
	HBITMAP hbmScreen = NULL;
	BITMAP bmpScreen;
	BOOL result = 1;

	// Retrieve the handle to a display device context for the client 
	// area of the window. 
	hdcScreen = GetDC(NULL);
	hdcWindow = GetDC(hWnd);

	// Create a compatible DC which is used in a BitBlt from the window DC
	hdcMemDC = CreateCompatibleDC(hdcWindow);

	if (!hdcMemDC)
	{
		printf("CreateCompatibleDC has failed");
		goto done;
	}
	/* do not need stretch mode here
	//This is the best stretch mode
	SetStretchBltMode(hdcWindow, HALFTONE);

	//The source DC is the entire screen and the destination DC is the current window (HWND)
	if (!StretchBlt(hdcWindow,
		0, 0,
		rcClient.right, rcClient.bottom,
		hdcScreen,
		0, 0,
		GetSystemMetrics(SM_CXSCREEN),
		GetSystemMetrics(SM_CYSCREEN),
		SRCCOPY))
	{
		//MessageBox(hWnd, L"StretchBlt has failed", L"Failed", MB_OK);
		printf("StretchBlt has failed");
		goto done;
	}
	*/
	// Create a compatible bitmap from the Window DC
	hbmScreen = CreateCompatibleBitmap(hdcWindow, rcClient.right - rcClient.left, rcClient.bottom - rcClient.top);

	if (!hbmScreen)
	{
		//MessageBox(hWnd, L"CreateCompatibleBitmap Failed", L"Failed", MB_OK);
		printf("CreateCompatibleBitmap Failed");
		goto done;
	}

	// Select the compatible bitmap into the compatible memory DC.
	SelectObject(hdcMemDC, hbmScreen);

	// Bit block transfer into our compatible memory DC.
	if (!BitBlt(hdcMemDC,
		0, 0,
		rcClient.right - rcClient.left, rcClient.bottom - rcClient.top,
		hdcWindow,
		0, 0,
		SRCCOPY))
	{
		//MessageBox(hWnd, L"BitBlt has failed", L"Failed", MB_OK);
		printf("BitBlt has failed");
		goto done;
	}

	// Get the BITMAP from the HBITMAP
	GetObject(hbmScreen, sizeof(BITMAP), &bmpScreen);

	BITMAPFILEHEADER   bmfHeader;
	BITMAPINFOHEADER   bi;

	bi.biSize = sizeof(BITMAPINFOHEADER);
	bi.biWidth = bmpScreen.bmWidth;
	bi.biHeight = bmpScreen.bmHeight;
	bi.biPlanes = 1;
	bi.biBitCount = 32;
	bi.biCompression = BI_RGB;
	bi.biSizeImage = 0;
	bi.biXPelsPerMeter = 0;
	bi.biYPelsPerMeter = 0;
	bi.biClrUsed = 0;
	bi.biClrImportant = 0;

	DWORD dwBmpSize = ((bmpScreen.bmWidth * bi.biBitCount + 31) / 32) * 4 * bmpScreen.bmHeight;

	// Starting with 32-bit Windows, GlobalAlloc and LocalAlloc are implemented as wrapper functions that 
	// call HeapAlloc using a handle to the process's default heap. Therefore, GlobalAlloc and LocalAlloc 
	// have greater overhead than HeapAlloc.
	HANDLE hDIB = GlobalAlloc(GHND, dwBmpSize);
	char *lpbitmap = (char *)GlobalLock(hDIB);

	// Gets the "bits" from the bitmap and copies them into a buffer 
	// which is pointed to by lpbitmap.
	GetDIBits(hdcWindow, hbmScreen, 0,
		(UINT)bmpScreen.bmHeight,
		lpbitmap,
		(BITMAPINFO *)&bi, DIB_RGB_COLORS);

	// A file is created, this is where we will save the screen capture.
	HANDLE hFile = CreateFile(filename,
		GENERIC_WRITE,
		0,
		NULL,
		CREATE_ALWAYS,
		FILE_ATTRIBUTE_NORMAL, NULL);

	// Add the size of the headers to the size of the bitmap to get the total file size
	DWORD dwSizeofDIB = dwBmpSize + sizeof(BITMAPFILEHEADER)+sizeof(BITMAPINFOHEADER);

	//Offset to where the actual bitmap bits start.
	bmfHeader.bfOffBits = (DWORD)sizeof(BITMAPFILEHEADER)+(DWORD)sizeof(BITMAPINFOHEADER);

	//Size of the file
	bmfHeader.bfSize = dwSizeofDIB;

	//bfType must always be BM for Bitmaps
	bmfHeader.bfType = 0x4D42; //BM   

	DWORD dwBytesWritten = 0;
	WriteFile(hFile, (LPSTR)&bmfHeader, sizeof(BITMAPFILEHEADER), &dwBytesWritten, NULL);
	WriteFile(hFile, (LPSTR)&bi, sizeof(BITMAPINFOHEADER), &dwBytesWritten, NULL);
	WriteFile(hFile, (LPSTR)lpbitmap, dwBmpSize, &dwBytesWritten, NULL);

	//Unlock and Free the DIB from the heap
	GlobalUnlock(hDIB);
	GlobalFree(hDIB);

	//Close the handle for the file that was created
	CloseHandle(hFile);

	//set result to 0, indicate it's a pass
	result = 0;

	//Clean up
done:
	DeleteObject(hbmScreen);
	DeleteObject(hdcMemDC);
	ReleaseDC(NULL, hdcScreen);
	ReleaseDC(hWnd, hdcWindow);

	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	BOOL result = 1;
	char* USAGE = "Usage:\n\tscreenshot.exe -h hWnd -f filename [-l left_coordinate][-r right_coordinate][-t top_coordinate][-b bottom_coordinate]";

	HWND hWnd = NULL;
	char* filename = NULL;
	int left, right, top, bottom;
	BOOL flag_hWnd = FALSE, flag_filename = FALSE;
	BOOL flag_left = FALSE, flag_right = FALSE, flag_top = FALSE, flag_bottom = FALSE;

	char* optstr = "h:l:r:t:b:f:";
	int	opt;

	while ((opt = getopt(argc, argv, optstr)) != -1)
	{
		switch (opt)
		{
		case 'h':
			flag_hWnd = TRUE;
			hWnd = (HWND)(atoi(optarg));
			break;
		case 'f':
			flag_filename = TRUE;
			filename = optarg;
			break;
		case 'l':
			flag_left = TRUE;
			left = atoi(optarg);
			break;
		case 'r':
			flag_right = TRUE;
			right = atoi(optarg);
			break;
		case 't':
			flag_top = TRUE;
			top = atoi(optarg);
			break;
		case 'b':
			flag_bottom = TRUE;
			bottom = atoi(optarg);
			break;
		case '?':
			printf(USAGE);
			break;
			return result;
		default:
			//should not go here
			break;
		}
	}

	if (!flag_hWnd || !flag_filename)
	{
		printf(USAGE);
		return result;
	}

	// Get the client area for size calculation
	RECT rcClient;
	GetClientRect(hWnd, &rcClient);

	// Get customer resize area
	if (flag_left && rcClient.left<left)
		rcClient.left = left;
	if (flag_right && rcClient.right>right)
		rcClient.right = right;
	if (flag_top && rcClient.top<top)
		rcClient.top = top;
	if (flag_bottom && rcClient.bottom>bottom)
		rcClient.bottom = bottom;

	//printf("%d, %d, %d, %d", rcClient.left, rcClient.right, rcClient.top, rcClient.bottom);

	result = CaptureAnImage(hWnd, rcClient, filename);
	return result;
}

