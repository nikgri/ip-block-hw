# Блокировка IP-адресов на HW-Coordinator

Данный скрипт был написан для автоматизации создания групп ip-объектов (до 1000 шт. в одном правиле) на HW-Coordinator

## Инструкция по использованию
1. При выполнении скрипта необходимо указать путь до файла с ip-адресами, которые необходимо заблокировать
2. Указать маску имени (например, block_list_: тогда первая группа ip-объектов будет называться block_list_0, и т.д.)
3. Указать количество ip-адресов в одной группе (на HW-Coordinator ограничение на максимальное количество ip-адресов в одной группе - 1000 шт.)

Результатом выполнения программы является файл result.txt, содержащий готовые к выполнению команды на HW-Coordinator в следующем виде:

```
firewall ip-object add name @your_ip_object_name_0 X.X.X.X,X.X.X.X,X.X.X.X....
firewall ip-object add name @your_ip_object_name_1 X.X.X.X,X.X.X.X,X.X.X.X....
...
```
