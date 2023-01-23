# FuckCpp
Do you want to ...?
1. Make your college confused when they read you c++ code?
2. Make your code messed up?
   
FuckCpp is a good choice.

### Installation
Run the batch installDependency.bat in folder js
Download the node.js runtime binary and decompress it to lib\win32

### Usage:
``` shell
Usage: fuckCpp file [options]...
Options:
    -h --help       Display This Help Info
    -v --version    Show FuckCpp build version

    -l <level>      Set confusion level to <level>, default value is 'low'
    -o <file>       Place the output into <file>, default value is 'confused.cpp'
    
    -z --zip        Zip the output source file
    --no-confuse    Ask FuckCpp not to confuse your source
```

Preview:
test.cpp
```cpp
#include <iostream>
using namespace std;
int main(int argc,const char *argv[]){
    printf("Hello,world");
    return 0;
}
```

Command: `fuckCpp test.cpp -o confused.cpp --zip`

confused.cpp:
```cpp
#define _0x47b5c7 scanf
#define _0x321c42 printf
#define _0xe7f261 cin
#define _0xa26408 cout
#define _0x1961c4 putchar
#define _0x2a8191 puts
#define _0x7862ee getchar
#define _0x7676b6 rand
#define _0x7a983c long long
#define _0xbca170 int
#define _0xbfbc05 const
#define _0x4b6b77 char
#define _0xc6c548 true
#define _0x7aff2b false
#define _0xe38a40 inline
#define _0x740124 struct
#define _0xd6c7f9 bool
#define _0x189995 __gcd
#define _0x7ad36d memset
#define _0x41ea93 NULL
#define _0x7f37d8 private
#define _0xc00564 public
#define _0x923466 void
#define _0xc4ebab while
#define _0xed1e31 for
#define _0x1b46fa auto
#define _0xcb0a86 size_t
#define _0xbe9935 if
#define _0xfcf52d return
#define _0xcbf09a else
#include<iostream>
using namespace std;_0xbca170 main(_0xbca170 argc,_0xbfbc05 _0x4b6b77*argv[]){_0x321c42("Hello,world");_0xfcf52d 0;}
```