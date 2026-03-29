t, l, r = map(int, input().split())
f = lambda n: n.bit_length()
print((t*(f(l)+(l-l)%2+f(l+1)+...+f(r)))-(l*f(r))%10**9+7)
