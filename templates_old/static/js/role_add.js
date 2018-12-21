$('#btn').on('click', function (e) {
            // 设置空数组
            var hobby = [];
            $('#hobby-group').find('input[type=checkbox]').each(function () {
                if ($(this).prop("checked")) {
                    var hobbyId = $(this).val();
                    hobby.push(hobbyId);
                }
            })
            console.log(hobby);
            $.ajax({
                'url': '/ajaxpost/',
                'method': 'post',
                'data': {
                    'username': $('.username').val(),
                    'hobby': hobby
                },
                'traditional': true,
                'beforeSend': function (xhr, settings) {
                    var csrftoken = ajaxpost.getCookie('csrftoken');
                    //2.在header当中设置csrf_token的值
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                },
                'success': function (data) {
                    console.log(data);
                }
            })
        })
