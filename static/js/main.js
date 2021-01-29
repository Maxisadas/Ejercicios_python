$(document).ready(function() {
   $('#enviar_ejercicio1').click(function(){
      const data = {
         "variable1":$('#variable1').val(),
         "variable2":$('#variable2').val(),
      }
      $.ajax({
         url:'/ejercicio1',
         type:'POST',
         dataTyoe:'json',
         data:data,
         success: function(res){
            $('#respuesta_ejercicio1').html(res);
         },
         error: function(XMLHttpRequest, textStatus, errorThrown) { 
            alert("Status: " + textStatus); alert("Error: " + errorThrown); 
        }   
      })

   })

   $('#enviar_ejercicio2').click(function(){
      const data = {
         "variable1":$('#variable1_ejercicio2').val(),
      }
      $.ajax({
         url:'/ejercicio2',
         type:'POST',
         dataTyoe:'json',
         data:data,
         success: function(res){
            $('#respuesta_ejercicio2').html(res);
         },
         error: function(XMLHttpRequest, textStatus, errorThrown) { 
            alert("Status: " + textStatus); alert("Error: " + errorThrown); 
        }   
      })

   })

   $('#enviar_ejercicio3').click(function(){
      const data = {
         "variable1":$('#variable1_ejercicio3').val(),
      }
      $.ajax({
         url:'/ejercicio3',
         type:'POST',
         dataTyoe:'json',
         data:data,
         success: function(res){
            $('#respuesta_ejercicio3').html(res);
         },
         error: function(XMLHttpRequest, textStatus, errorThrown) { 
            alert("Status: " + textStatus); alert("Error: " + errorThrown); 
        }   
      })

   })

});