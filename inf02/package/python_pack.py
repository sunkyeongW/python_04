print('---' * 7)
print("파이썬 패키지")
print()

import sub.sub1.module1
import sub.sub2.module2

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print('---' * 7)
print("from과 as 이용")
print()

from sub.sub1 import module1 as mo1
from sub.sub2 import module2 as mo2

mo2.mod2_test1()
mo2.mod2_test2()
print()

from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module2.mod2_test1()

print('---' * 7)
print("__init__.py")
print("사용 권한을 지정해줌")




