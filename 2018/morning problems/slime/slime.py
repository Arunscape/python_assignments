num = int ( input () )

out = list()
while num > 0:
  num-=1
  out.append(1)
  if len(out) ==1:
      continue

  # print(out[-2], out[-1])
  while out[-2] == out[-1]:
      if out[-2]==out[-1]:
          out[-2] += 1
          del out[-1]
      if len(out) ==1:
          break

print(*out)
