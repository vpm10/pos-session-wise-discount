odoo.define('pos_session_discount.Pos', function(require) {
    "use strict";
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');
    var session_sum = 0;
    const limit_discount = (ProductScreen) => class extends ProductScreen {
        async _onClickPay() {
            var category_values = 0;
            var discount_value = this.env.pos.config.discount;
            const disc = []
            await rpc.query({
                model: 'pos.config',
                method: 'get_categories',
            }).then(function(result) {
                category_values = result;
                });
            $.each(this.env.pos.selectedOrder.selected_orderline.order.orderlines,function(index, name){
                    if (category_values.includes(name.product.pos_categ_id[0])){
                            var total = name.price * name.quantity
                            disc.push(total*(name.discount/100))
                    }
                })
               var sum = 0;
                disc.forEach(x => { sum += x; });
                session_sum += sum
                if(session_sum > discount_value){
                    session_sum -= sum
                    console.log(session_sum)
               this.showPopup("ErrorPopup", {
                      title: 'Discount Limit Exceeded.!!',
                      body: 'Discount Limit is: ' + this.env.pos.config.discount,
                  });
                  }
               else{ console.log('aaa'), super._onClickPay()}
        }
    }
    Registries.Component.extend(ProductScreen, limit_discount);
    return ProductScreen;
});