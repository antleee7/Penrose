# 진짜 단순한 건데, gamma로 xi 만드는 코드입니다.
# xi로 AR pattern 만드는 건 생각보다 어렵네요... 열심히 해보겠습니다.

import cmath

def gamma_to_xi(gamma_0, gamma_1, gamma_2, gamma_3, gamma_4):
    zeta = cmath.exp(2j * cmath.pi / 5)

    if (gamma_0 + gamma_1 + gamma_2 + gamma_3 + gamma_4) == 0:
        result = sum(gamma_n * zeta**(2*n) for n, gamma_n in enumerate([gamma_0, gamma_1, gamma_2, gamma_3, gamma_4]))
        return result
    else:
        return None
