# Блокировка IP-адресов на HW-Coordinator

Данный скрипт был написан для автоматизации создания групп ip-объектов на HW-Coordinator

## Инструкция по использованию
1. При выполнении скрипта необходимо указать путь до файла с ip-адресами, которые необходимо заблокировать (скрипт способен воспринять список ip-адресов практически в любом виде,но пример как желательно должен выглядять файл есть в репозитории. Путь до txt файла не должен содержать пробелов, поэтому лучше подкинуть его в одну папку со скриптом)
2. Указать маску имени (например, block_list_: тогда первая группа ip-объектов будет называться block_list_1, и т.д. Также можно начать и с произвольного номера, например, block_list_33, с которого начнется отсчет)
3. Указать количество ip-адресов в одной группе (на HW-Coordinator ограничение на максимальное количество ip-адресов в одной группе - 1000 шт.)
При выполнении скрипт автоматически удаляет повторяющиеся ip-адреса.

Результатом выполнения программы является файл result.txt, содержащий готовые к выполнению команды на HW-Coordinator в следующем виде:

```
firewall ip-object add name @your_ip_object_name_1 X.X.X.X,X.X.X.X,X.X.X.X....
firewall ip-object add name @your_ip_object_name_2 X.X.X.X,X.X.X.X,X.X.X.X....
...
```
