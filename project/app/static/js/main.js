var app = {
	init: function(){
		init.main();
		var page = $('body').attr('data-page');
		if (typeof init[page] == 'function'){
			init[page]();
		}
	}
}

var init = {
	main: function(){

	},
	index: function(){

	},
	product: function(){
		$('#input-date').datetimepicker({
			format: 'DD.MM.YYYY',
			useCurrent: false
		});

		var $form = $('#form-product');
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

		$('#input-name, #input-address, #input-date')
			.bind('checkValid', function(){
				changeClass(this, this.value.trim().length > 1, true);
			})
			.bind('checkValidWithoutDanger', function(){
				changeClass(this, this.value.trim().length > 1, false);
			});

		$('#input-count')
			.bind('checkValid', function(){
				changeClass(this, this.value.match(/^[0-9]+$/), true);
			})
			.bind('checkValidWithoutDanger', function(){
				changeClass(this, this.value.match(/^[0-9]+$/), false);
			});

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

	}
}

$(document).ready(function(){
	app.init();
})
