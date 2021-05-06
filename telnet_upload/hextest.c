#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char byte;
typedef unsigned int uint;

byte ConvQueryParam(byte query_param)
{
    if ((query_param < '0') || ('9' < query_param))    // if not digit
    {
        if ((query_param < 0x41) || (0x46 < query_param)) // if not A-F
        {
            if ((0x60 < query_param) && (query_param < 0x67)) // if not a-f
            {
                query_param = query_param + 0xa9; 
            }
        }
        else // is A-F
        {
            query_param = query_param - 0x37;
        }
    }
    else // is digit 
    {
        query_param = query_param - 0x30;
    }
    return query_param;
}
bool urldecode(char *query)
{
  char cChar;
  size_t lQueryLen;
  bool bProperQuery;
  char convertedQuery [20483];
  char temp;
  int queryOutputIndex;
  uint queryInputIndex;
  if ((query == (char *)0x0) || (lQueryLen = strlen(query), 0x4fff < lQueryLen)) {
    bProperQuery = 0;
  }
  else {
    queryOutputIndex = 0;
    queryInputIndex = 0;
    while (lQueryLen = strlen(query), queryInputIndex < lQueryLen) {
      if (query[queryInputIndex] == '%') { 
        cChar = query[queryInputIndex + 2];
        temp = ConvQueryParam(query[queryInputIndex + 1]);
        temp = temp << 4;
        cChar = ConvQueryParam(cChar);
        temp = temp + cChar;
        convertedQuery[queryOutputIndex] = temp;
        queryInputIndex = queryInputIndex + 2;
      }
      else {
        convertedQuery[queryOutputIndex] = query[queryInputIndex];
      }
      queryOutputIndex = queryOutputIndex + 1;
      queryInputIndex = queryInputIndex + 1;
    }
    convertedQuery[queryOutputIndex] = '\0';
    strcpy(query,convertedQuery);
    bProperQuery = 1;
  }
  return bProperQuery;
}

int main(int argc, char *argv[])
{   
    if(argc<2)
    {
        printf("usage %s url\n", argv[0]);
        exit(-1);
    }
    char query[2000];
    strcpy(query, argv[1]);
    urldecode(query);
    printf("%s\n", query);

    return 0;
}