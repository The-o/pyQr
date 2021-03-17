# Что это такое

Програма, позволяющая читать QR-коды с экрана и копировать их содержимое в буфер обмена, а также позволяющая генерировать QR-коды из текста, содержащегося в буфере обмена.

# Установка

Для работы и установки pyQr необходим установленный python3!

## С помощью pip из github'а
```sh
pip3 install git+https://github.com/The-o/pyQr.git@master
```

## С помощью pip локально

1. Скачать скрипты [pqQr](https://raw.githubusercontent.com/The-o/pyQr/master/pyQr) и [setup.py](https://raw.githubusercontent.com/The-o/pyQr/master/setup.py) в пустую директорию

2. В этой директории выполнить:
    ```sh
    pip3 install .
    ```

## Руками

1. Скачать скрипт [pqQr](https://raw.githubusercontent.com/The-o/pyQr/master/pyQr)

2. Установить зависимости:
    ```sh
    pip3 install pyzbar wxPython qrcode
    ```
## Если в Ubuntu pip ругается при установке wxPython:

```sh
sudo apt install python3-wxgtk4.0
```

Потом повторить установку выбранным способом

# Запуск:

## После установки с помощью pip
Из командной строки:

```sh
pyQr
```
## После установки руками
Из командной строки:

```sh
python3 <путь, куда был скачан скрипт pyQr>
```

## Если в Ubuntu будет ругаться "Unable to find zbar shared library":

```sh
sudo apt install libzbar0
```
# Как использовать:

После запуска в системном трее появится иконка ![в виде QR-кода](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5QMWFQQCKACXsQAABHxJREFUOMt9lV9IVHkUxz+/uXNndJxRR29u9sf8h81so2Nh2b9xl0YiKAQfYtkgeujPQkR/rBfrqbfFanuLFjLwoSCCjJAIUrSsdjPTRdBRiVWbInAb8Y4zd2a8d+buQ1u7ruyepwPnnA8czvecIwzDMFVV5d8mhCA3N5dEIoHT6QQgFouRnZ1NNBrFNM1lNXl5eVhVVWXfvn0Eg8Elwc7OTnp6emhvb+f48eMAPH78mMbGRgKBAM3NzUvye3p66OrqwgoQDAY5ffo009PTAHi9Xnq7uxHAjbY2vB4PALV+P263m3yXi9bWVkKhEAClpaVfwNbPzvT0NHV1ddglialwGKcs43S5+PHaNcaHhwGo9vkAcMoyqqqyo76eVDrN4ODgciCAXZIocjgQQIEskzEMVuTn49u/H4DwmzesXLmSAllGAEUOB7OatqT1L0Cv18tUOIwAChWFQpuNLIeDVatXM/zwIQAzIyPU1NVRaLNRqCgMTExg/jWM+/fvfwIKIejs7KS3uxunLFMgyxTabLhlmbiq8sfYGJsaGgBQCgqQhMAty7Q0NRFZXGRO14npOvMLC7S0tCAMwzCj0Shut5t4LEZC0xCAJAQSEJ2ZYerWLexr1hCZnMR/5gzFHg+GYZDUNCxWK7GFBUxAURSsiUSC7u5uav1+fnn6lLl37yhfuxaXJJGTTGJ5/pz1Bw+yYvdu3ty+TbivD4vNhsXh4Ne+PtbX1vLT5cuUlJdz8uRJrE6nk61btxL0+/nh7Fl27tpFXk4OdiHIymQQubm4JOlTy9XV5KRSPLt6lW8uXMAiBPluN2UVFXzt8yHLMiIej5u9vb0UFRURj0Z5/egR8Rcv+P7KFdwFBbiLizHHxzGiUaSNG1E/fkRLpSiqrCQyO8vM27f8PjVFlceD3+/HkkwmGRkZYfPmzRi6Tk1DA19t3054bAylqgrJ5UJ4PFBRgSUrC6WqiveTk2RlZ7N63TpMYDwUYmhoCF3Xlw/FarWSSiTIGAay1crQjRtkWSwAJDMZNh05gqZpDDx5wt4DB3jW308ymaS6pgZFURBzc3NmIBAg3+VaJpuW9naGu7r49tAhDF3nSUcHv927R2bVKkZfv2Zelnk/P8/Pd+7g8/mw2WxYTdOkubmZ1tZWVFX9IuyWpibSpslCJkMqlaLv7l36b95kdTDI3sOHuXDsGFt27sQwTVKpFBcvXuTcuXN/b0ooFGJHfT1FDgcDExNEFhcxgXgmw+ToKHcvXULPZDhz6hT9vb18d+IEJWVlAHz48IENGzZgt9uX7nIqnWZW0zCBOV0n2+GgessWFhcXqT96lPKqKrIdDtaUleHxeuno6CASiRAIBCgpKUGSJCyfYaWlpQwODvL85Uvy8vKI6To5Tic+v580sHHbNhr37GHg1SsutbVhmiaVlZUEAgEePHhAQ0MDmqYhIpGI+V8Htr+/n+vXrxMOhwE4f/48siyTTqdRFIVYLMbo6CjRaJSamhqKi4s/yeb/XsA/Yy6XC1mWl+Qlk0mEENjtdgD+BIUh11qhyPEpAAAAAElFTkSuQmCC).

При клике на неё правой кнопкой мыши в случае, если на экране отображаются QR-коды:
* Экран затемнится кроме распознанных QR-кодов;
* По наведению на распознанный QR-код будет отображена всплывающая подсказка с распознанным текстом;
* При клике на распознанный QR-код его текст будет скопирован в буфер обмена
* При клике вне распознанного QR-кода, затемнение экрана исчезнет, в буфер ничего не скопируется

При клике левой кнопкой мыши откроется меню с двумя пунктами:
* QR
* Выход

При клике на пункт "QR", если в буфере обмена есть текст, будет сгенерирован и отбражён QR-код в новом окне. По клику на QR-код окно будет закрыто. Если в буфере обмена нет текста или размер текста превышает 2953 байт, будет выведено сообщение.

При клике на пункт Выход произойдёт выход из программы.
