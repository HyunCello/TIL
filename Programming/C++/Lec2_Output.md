# Hello World, Namespace

Old(C)
```c
printf("Hello,%s%d\n, "world",123);
```
New (C++)
```c++
std::cout << "Hello, " << "world" << 123 << std::endl;
```
## std::cout, std::endl
```c++
#include <iostream>

int main()
{
    std::cout << "hello, world!" << std::endl;

    return 0;
}
```
## Namespace
- java의 패키지, C#의 네임스페이스와 비슷
- 이런 것들과의 충돌을 피하기 위해
    - 함수
    - 클래스
    - 기타 등등
    ```c++
        namespace hello
        {
            void PrintHelloWorld();
        }
    ```
### Namespace 예제

#### OLD
```c
// Hello1.h
void SayHello();

// Hello2.h
void SayHello();

// Main.cpp
#include "Hello1.h"
#include "Hello2.h"

// ...

SayHello(); // 컴파일 오류!!!

```
#### New
```c++
namespace hello
{
    void SayHello();
}
namespace hi
{
    void SayHello();
}
// ...

hello::SayHello();
hi::SayHello();

```
## Using 지시문
- Java의 *import*나 C#의 *using*과 비슷
- 타이핑의 양을 줄이는 방법일 뿐

### using 예제
using 사용하지 않는 경우
```c++
#include <iostream>

int main()
{
    std::cout << "hello, world!" << std::endl;

    return 0; 
}
```
using 사용하는 경우
```c++
#include <iostream>

using namespace std;

int main()
{
    cout << "hello, world!" << endl;

    return 0; 
}
```