$(function(){
    var html = $('info');
    $("#btn1").click(function(){ 
        $("#info").html("<div>{% if not doc_nevrop %}<h1>Невропатологов нет!</h1>{%else%} {% for d in doc_nevrop %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn2").click(function(){ 
        $("#info").html("<div>{% if not doc_androl %}<h1>Андрологов нет!</h1>{%else%} {% for d in doc_androl %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn3").click(function(){ 
        $("#info").html("<div>{% if not doc_aneste %}<h1>Анестезиологов нет!</h1>{%else%} {% for d in doc_aneste %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn4").click(function(){ 
        $("#info").html("<div>{% if not doc_venero %}<h1>Венерологов нет!</h1>{%else%} {% for d in doc_venero %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn5").click(function(){ 
        $("#info").html("<div>{% if not doc_gastro %}<h1>Гастроэнтерологов нет!</h1>{%else%} {% for d in doc_gastro %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn6").click(function(){ 
        $("#info").html("<div>{% if not doc_gineko%}<h1>Гинекологов нет!</h1>{%else%} {% for d in doc_gineko %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn7").click(function(){ 
        $("#info").html("<div>{% if not doc_kardio %}<h1>Кардиологов нет!</h1>{%else%} {% for d in doc_kardio %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn8").click(function(){ 
        $("#info").html("<div>{% if not doc_logope %}<h1>Логопедов нет!</h1>{%else%} {% for d in doc_logope %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn9").click(function(){ 
        $("#info").html("<div>{% if not doc_mammol %}<h1>Маммологов нет!</h1>{%else%} {% for d in doc_mammol %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn10").click(function(){ 
        $("#info").html("<div>{% if not doc_nevrol %}<h1>Неврологов нет!</h1>{%else%} {% for d in doc_nevrol %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn11").click(function(){ 
        $("#info").html("<div>{% if not doc_neuroh %}<h1>Нейрохирургов нет!</h1>{%else%} {% for d in doc_neuroh %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn12").click(function(){ 
        $("#info").html("<div>{% if not doc_otolor %}<h1>Отоларингологов нет!</h1>{%else%} {% for d in doc_otolor %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn13").click(function(){ 
        $("#info").html("<div>{% if not doc_oftalm %}<h1>Офтальмологов нет!</h1>{%else%} {% for d in doc_oftalm %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn14").click(function(){ 
        $("#info").html("<div>{% if not doc_pediat %}<h1>Педиатров нет!</h1>{%else%} {% for d in doc_pediat %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn15").click(function(){ 
        $("#info").html("<div>{% if not doc_prokto%}<h1>Проктологов нет!</h1>{%else%} {% for d in doc_prokto %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn16").click(function(){ 
        $("#info").html("<div>{% if not doc_terapi %}<h1>Терапевтов нет!</h1>{%else%} {% for d in doc_terapi %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn17").click(function(){ 
        $("#info").html("<div>{% if not doc_urolog %}<h1>Урологов нет!</h1>{%else%} {% for d in doc_urolog %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn18").click(function(){ 
        $("#info").html("<div>{% if not doc_hirurg %}<h1>Хирургов нет!</h1>{%else%} {% for d in doc_hirurg %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
    $("#btn19").click(function(){ 
        $("#info").html("<div>{% if not doc_endokr %}<h1>Эндокринологов нет!</h1>{%else%} {% for d in doc_endokr %}<h1>{{d.name}}</h1>{%endfor%} {%endif%}")

    });
});