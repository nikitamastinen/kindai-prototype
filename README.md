# KindAI (прототип)
Наше решение позволяет оценивать сообщения в корпоративных чатах на предмет токсичности/доброты
и отзывчивости/пассивности.

В демо-версии возвращается ответ в формате

```
{
    "уровень отзывчивости": {-10 ... 10},
    "уровень токсичности": {-10 ... 10},
    "рекомендация HR": {...},
    "рекомендация сотруднику": {...}"
}
```

Для простоты запуска ключи оставлены в коде. Просьба этим не злоупотреблять.