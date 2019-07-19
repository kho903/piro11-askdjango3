
import os
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView



class PostListView1(View):
    def get(self, request):
        name = '지훈'
        html=self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>AskDjango</h1>
            <p>{name}</p>
            <p>가나다라마바사아자차카타파하</p>
        '''


post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context= super().get_context_data()
        context['name']= '지훈'
        return context

post_list2= PostListView2.as_view()


class PostListView3(View):
    # CBV: JSON 형식 응답하기
    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii' : False})

    def get_data(self):
        return{
            'massage': '안녕, 파이썬&장고',
            'items' : ['파이썬','장고','Celery','Azure', 'AWS'],
        }

post_list3= PostListView3.as_view()



class ExcelDownloadView(View):

    excel_path= 'C:/dev/askdjango/gdplev.xls'

    def get(self,request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
            #필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment; filename ="{}"'.format(filename)
            return response

excel_download = ExcelDownloadView.as_view()