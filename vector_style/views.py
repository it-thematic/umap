from django.http import JsonResponse
from .models import DatalayerStyles, Styles


def get_datalayer_styles(request, datalayer):
    """
    Получение списка стилей для слоя
    :param request: объекта запроса
    :param datalayer: id слоя
    :return: list of id:title (id стиля: заголовок стиля
    """
    response = {'data': list()}

    # Пока все exception выдают пустой список и 200. Если надо можно сделать разные ответы
    try:
        datalayer_styles = DatalayerStyles.objects.get(datalayer=datalayer)
    except DatalayerStyles.DoesNotExist:
        return JsonResponse(data=response)
    except Exception as e:
        return JsonResponse(data=response)

    for style in Styles.objects.filter(pk__in=datalayer_styles.styles.split(',')):
        response['data'].append((str(style.id), style.title))
    response['data'].sort()
    return JsonResponse(data=response, safe=True, status=200)


def get_datalayer_style(request, datalayer, style):
    """
    Получение выбранного стиля для слоя
    :param request: оъект запроса
    :param datalayer: id слоя
    :param style: id стиля
    :return: json: описания стиля в формате JSON
    """
    response = {}
    try:
        datalayer_styles = DatalayerStyles.objects.get(datalayer=datalayer)
    except DatalayerStyles.DoesNotExist:
        return JsonResponse(data=response)

    try:
        styles = Styles.objects.filter(pk__in=datalayer_styles.styles.split(',')).get(pk=style)
    except Styles.DoesNotExist:
        return JsonResponse(response)
    return JsonResponse(data=styles.style, safe=True, status=200)
