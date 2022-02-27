from rest_framework.test import APITestCase

from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTesteCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',descricao='Curso teste 1', nivel='B')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT2',descricao='Curso teste 1', nivel='A')   

    # def test_falhador(self):
    #     self.fail("teste falhou de propósito, não se preoucupe Uilan")

    def test_requisicao_get_listar_cursos(self):
        """test verificar requisição para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
    
    def test_requisica_post_para_criar_curso(self):
        """test verificar requisição post para criar cursos"""
        data ={
            'codigo_curso':"CTT3",
            'descricao':'Curso teste 3',
            'nivel':'I'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertAlmostEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisica_delete_para_deletar_curso(self):
        """test verificar requisição delete para não permitir deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_curso(self):
        """Teste  de requisição  verificação put para atualizar um curso """
        data ={
            'codigo_curso':'CTT1',
            'descricao':'cursos test1 atualizado',
            'nivel':"I"
        }
        response = self.client.put('/cursos/1/',data=data)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
