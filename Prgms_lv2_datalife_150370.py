def solution(today, terms, privacies):
  answer = []
  tdyear, tdmonth, tdday = map(int, today.split('.'))

  # terms_re을 dict comprehension을 이용하여 한 줄로 표현
  terms_re = {word: int(month) for word, month in map(str.split, terms)}

  for idx, priv in enumerate(privacies, 1):
    datedata, word = priv.split(" ")
    year, month, day = map(int, datedata.split("."))
    month += terms_re[word]
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1
    if year > tdyear or (year == tdyear and
                         (month > tdmonth or
                          (month == tdmonth and day > tdday))):
      continue
    answer.append(idx)

  return sorted(answer)
