from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Medicina(models.Model): #Медицина
#    name = models.CharField(max_length = 100, unique=True, null=False, verbose_name='Название')
#    image = models.CharField(max_length = 100, unique=True, null=False, verbose_name='Ссылка на фото')
#    title_information = models.TextField(verbose_name='Оглавление')
#    full_information = models.TextField(verbose_name='Полный текст')
#    def __str__(self):
#        return self.name
#    class Meta:
#        verbose_name = 'Медицина'
#        verbose_name_plural = 'Медицины'
#        ordering = ['name']
class WorkGrafic(models.Model):
    time_work = (
        ('1', 'Выходной'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    )
    monday_start = models.CharField(max_length=20, verbose_name='Понедельник начало работы', choices=time_work, default='8')
    monday_stop = models.CharField(max_length=20, verbose_name='Понедельник конец работы', choices=time_work, default='17')
    tuesday_start = models.CharField(max_length=20, verbose_name='Вторник начало работы', choices=time_work, default='8')
    tuesday_stop = models.CharField(max_length=20, verbose_name='Вторник конец работы', choices=time_work, default='17')
    wednesday_start = models.CharField(max_length=20, verbose_name='Среда начало работы', choices=time_work, default='8')
    wednesday_stop = models.CharField(max_length=20, verbose_name='Среда конец работы', choices=time_work, default='17')
    thursday_start = models.CharField(max_length=20, verbose_name='Четверг начало работы', choices=time_work, default='8')
    thursday_stop = models.CharField(max_length=20, verbose_name='Четверг конец работы', choices=time_work, default='17')
    friday_start = models.CharField(max_length=20, verbose_name='Пятница начало работы', choices=time_work, default='8')
    friday_stop = models.CharField(max_length=20, verbose_name='Пятница конец работы', choices=time_work, default='17')
    saturday_start = models.CharField(max_length=20, verbose_name='Суббота начало работы', choices=time_work, default='8')
    saturday_stop = models.CharField(max_length=20, verbose_name='Суббота конец работы', choices=time_work, default='17')
    weekend_one_people_start = models.TextField(verbose_name='Отпуск начало (дд.мм.гг)', default='07.08.2019')
    weekend_one_people_stop = models.TextField(verbose_name='Отпуск конец (дд.мм.гг)', default='08.09.2019')
    weekend = models.TextField(verbose_name='Выходные дни (дд.мм)', default='8.03, 31.12, 23.02')
    
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графикы работы'

class Medicina(models.Model):
    name = models.CharField(max_length = 100, unique=True, null=False, verbose_name='Название')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Медицина'
        verbose_name_plural = 'Медицины'
        ordering = ['name']

class Service(models.Model):
    name = models.CharField(max_length = 400, unique=True, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.CharField(max_length = 100, verbose_name='Ссылка на фото')
    text = models.TextField(verbose_name='Описание', null=True, blank=True)
    medicina = models.ForeignKey(Medicina, on_delete=models.SET_NULL, verbose_name='Услуги', related_name='services', null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

class Doctor(models.Model): #Доктор
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    father_name = models.CharField(max_length = 50, verbose_name='Отчество')
    photo = models.CharField(max_length = 200, null=True)
    medicina = models.ForeignKey(Medicina, on_delete=models.SET_NULL, verbose_name='Медицина', related_name='doctors', null=True, blank=True)
    majors = (
        ('Андролог','Андролог'),
        ('Анестезиолог','Анестезиолог'),
        ('Венеролог','Венеролог'),
        ('Гастроэнтеролог','Гастроэнтеролог'),
        ('Гинеколог','Гинеколог'),
        ('Маммолог','Маммолог'),
        ('Неврапотолог','Неврапотолог'),
        ('Невролог','Невролог'),
        ('Нейрохирург','Нейрохирург'),
        ('Логопед','Логопед'),
        ('Кардиолог','Кардиолог'),
        ('Оториноларинголог','Оториноларинголог'),
        ('Офтальмолог','Офтальмолог'),
        ('Педиатр','Педиатр'),
        ('Проктолог','Проктолог'),
        ('Терапевт','Терапевт'),
        ('Уролог-андролог','Уролог-андролог'),
        ('Хирург','Хирург'),
        ('Эндокринолог','Эндокринолог'),
    )
    major = models.CharField(max_length=100, verbose_name='Специальность', choices=majors, default='Терапевт')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы')
    def __str__(self):
        fio = self.surname+' '+self.name+' '+self.father_name
        return fio
    
    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['name']

class Patient(models.Model): #Пациент
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь',null=True, related_name='patient')
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    gender = models.CharField(max_length=5, choices=(('муж','Муж'),('жен','Жен')), verbose_name='Пол')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')
    birthday = models.DateField()
    blood_group = models.CharField(max_length=5, verbose_name='Группа крови',choices=(('-1','-1'),('-2','-2'),('-3','-3'),('-4','-4'),('+1','+1'),('+2','+2'),('+3','+3'),('+4','+4')))
    def __str__(self):
        namea = self.surname+' '+self.name+'.'+self.second_name 
        return namea
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['surname']

class Analysis(models.Model): #Анализы
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    laboratory = models.CharField(max_length=200, verbose_name='Лаборатория')
    result = models.TextField(verbose_name='Резултат')
    priority = models.TextField(verbose_name='Приоритет')
    out_patient_card = models.ForeignKey('OutPatientCard', on_delete=models.PROTECT, verbose_name='Амбулаторная карта', related_name='analyse')
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Врач', related_name='analyse')
    assistent = models.ForeignKey('Assistent', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Лаборант', related_name='analyse')
    def __str__(self):
        return self.date.strftime('%d-%m-%Y')
    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ['date']

class Assistent(models.Model): #Лаборант
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+'.'+self.second_name 
        return namea
    class Meta:
        verbose_name = 'Лаборант'
        verbose_name_plural = 'Лаборанты'
        ordering = ['surname']

class Contract(models.Model): #Договор
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    price = models.IntegerField(verbose_name='Стоимость')
    status = models.CharField(max_length=100, verbose_name='Статус')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, verbose_name='Пациент')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', null=True)
    assistant = models.ForeignKey(Assistent, on_delete=models.PROTECT, verbose_name='Лаборант', null=True)
    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
        ordering = ['date']

class Visit(models.Model): #Посещения   
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    number = models.IntegerField(verbose_name='Количество посещений')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, verbose_name='Пациент',)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', related_name='visit')
    cashier = models.ForeignKey('Cashier', on_delete=models.PROTECT, verbose_name='Кассир', related_name='visit')
    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
        ordering = ['date']

class OutPatientCard(models.Model): #Амбулаторная карта
    number_police = models.CharField(unique=True, max_length=30, verbose_name='Номер страх. полиса')
    passport = models.TextField(unique=True, verbose_name='Паспортные данные')
    company = models.CharField(max_length=50, verbose_name='Страх. компания')
    record = models.TextField(verbose_name='Записи')
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Пациент', related_name='out_patient_card')
    def __str__(self):
        return self.number_police
    class Meta:
        verbose_name = 'Амбулаторная карта'
        verbose_name_plural = 'Амбулаторные карты'
        ordering = ['number_police']

class Cashier(models.Model): #Кассир
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+'.'+self.second_name
        return namea
    class Meta:
        verbose_name = 'Кассир'
        verbose_name_plural = 'Кассиры'
        ordering = ['surname']

class MedRequest(models.Model): #Заявка
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=50, verbose_name='Статус')
    assistent = models.ForeignKey(Assistent, on_delete=models.CASCADE, verbose_name='Лаборант', null=True, related_name='med_request')
    medsister = models.ForeignKey('MedSister', on_delete=models.CASCADE, verbose_name='Медсестра', null=True, related_name='med_request')
    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['date']

class Reception(models.Model): #Прием
    datetime = models.DateTimeField(verbose_name='Дата и время приема')
    status = models.CharField(max_length=50, verbose_name='Статус')
    registrator = models.CharField(max_length=225, verbose_name='Регистратор', null=True)
    patient = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач')
    def __str__(self):
        return self.datetime.strftime("%d-%b-%Y (%H:%M)")
    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'
        ordering = ['datetime']

class RegistryClerk(models.Model): #Регистратура
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+'.'+self.second_name
        return namea
    class Meta:
        verbose_name = 'Ригистратор'
        verbose_name_plural = 'Ригистраторы'
        ordering = ['surname']

class MedSister(models.Model): #Мед сестра
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Медсестра', null=True)
    def __str__(self):
        namea = self.surname+' '+self.name+'.'+self.second_name
        return namea
    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'
        ordering = ['surname']

class Treatment(models.Model): #Лечение Обращение
    date = models.DateField(verbose_name='Дата')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач')
    patient_card = models.ForeignKey(OutPatientCard, on_delete=models.PROTECT, verbose_name='Амбулаторная карта')
    diagnose = models.TextField(verbose_name='Диагноз')
    medication = models.TextField(verbose_name='Лечение')
    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['date']

