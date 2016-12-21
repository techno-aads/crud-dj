var app = {
	init: function(){
		init.main();
		var page = $('body').attr('data-page');
		if (typeof init[page] == 'function'){
			init[page]();
		}
	},
	regex: {
		email: /^[^\@]+@[^\@]+$/,
		login: /^([a-z0-9]+[\.\-]?){3,}$/i
	}
}

var init = {
	main: function(){

	},
	index: function(){

	},
	login: function(){

		init.func.validForm($('#form-login'), [
			{
				$el: $('#input-login'),
				validate: function(_this){
					return _this.value.match(app.regex.login);
				}
			},{
				$el: $('#input-password'),
				validate: function(_this){
					var value = _this.value;
					var b = value.match(/[a-z]/);
					b = b && value.match(/[A-Z]/);
					b = b && value.match(/[0-9]/);
					b = b && (value.length > 7);
					return b;
				}
			}
		]);
	},
	registration: function(){

		init.func.validForm($('#registration-form'), [
			{
				$el: $('#input-email'),
				validate: function(_this){
					return _this.value.match(app.regex.email);
				}
			},{
				$el: $('#input-login'),
				validate: function(_this){
					return _this.value.match(app.regex.login);
				}
			},{
				$el: $('#input-password'),
				validate: function(_this){
					$('#input-password-repeat').trigger('input');
					var value = _this.value;
					var b = value.match(/[a-z]/);
					b = b && value.match(/[A-Z]/);
					b = b && value.match(/[0-9]/);
					b = b && (value.length > 7);
					return b;
				}
			},{
				$el: $('#input-password-repeat'),
				validate: function(_this){
					var value = _this.value;
					var b = value.match(/[a-z]/);
					b = b && value.match(/[A-Z]/);
					b = b && value.match(/[0-9]/);
					b = b && (value.length > 7);
					b = b && (value == $('#input-password').val());
					return b;
				}
			}
		]);
	},
	product: function(){
		$('#input-date').datetimepicker({
			format: 'DD.MM.YYYY',
			useCurrent: false
		});

		init.func.validForm($('#form-product'), [
			{
				$el: $('#input-count'),
				validate: function(_this){
					return _this.value.match(/^[0-9]+$/);
				}
			},{
				$el: $('#input-name, #input-address, #input-date'),
				validate: function(_this){
					return _this.value.trim().length > 1;
				}
			}
		]);

		var $removeForm = $('#remove-form');
		var $modal = $('#modal-remove');
		var modalOpened = false;
		$modal.bind('show.bs.modal', function(){
			modalOpened = true;
		});
		$modal.bind('hide.bs.modal', function(){
			modalOpened = false;
		});
		$('#modal-no').bind('click', function(){
			$modal.modal('hide');
		});
		$('#modal-yes').bind('click', function(){
			$removeForm.trigger('submit');
		});
		$removeForm.bind('submit', function(){
			if (!modalOpened){
				$modal.modal('show');
				return false;
			}
		})
	},
	products: function(){

	},
	func: {
		validForm: function($form, data){
			var $checkValid = $form.find('.check-valid');
			var $inputs = $checkValid.find('.input-valid');

			var changeClass = function(el, state, addError){
				var $wrap = $(el).closest($checkValid);
				$wrap.removeClass('has-success has-error');
				if (state){
					$wrap.addClass('has-success');
				} else if (addError){
					$wrap.addClass('has-error');
				}
			}

			data.forEach(function(element){
				element.$el
					.bind('checkValid', function(){
						changeClass(this, element.validate(this), true);
					})
					.bind('checkValidWithoutDanger', function(){
						changeClass(this, element.validate(this), false);
					});
			})

			$inputs.bind('focusout', function(){
				$(this).trigger('checkValid');
			});
			$inputs.bind('focus input', function(){
				$(this).trigger('checkValidWithoutDanger');
			});

			$inputs.trigger('checkValidWithoutDanger');

			$form.bind('submit', function(){
				$inputs.trigger('checkValid');
				if ($form.find('.check-valid.has-error').length){
					return false;
				}
			})
		}
	}
}

$(document).ready(function(){
	app.init();
})
