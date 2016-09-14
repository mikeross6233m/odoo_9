class HotelFloor(models.Model):

    _name = "hotel.floor"
    _description = "Floor"

    name = fields.Char('Floor Name', size=64, required=True, select=True)
    sequence = fields.Integer('Sequence', size=64)


class ProductCategory(models.Model):

    _inherit = "product.category"

    isroomtype = fields.Boolean('Is Room Type')
    isamenitytype = fields.Boolean('Is Amenities Type')
    isservicetype = fields.Boolean('Is Service Type')


class HotelRoomType(models.Model):

    _name = "hotel.room.type"
    _description = "Room Type"

    cat_id = fields.Many2one('product.category', 'category', required=True,
                             delegate=True, select=True, ondelete='cascade')

