const mongoose = require('mongoose');

const register_schema = new mongoose.Schema({
    Full_name:{
        type:String,
        required:true
    },
    Email:{
        type:String,
        required:true
    },
    Family_income:{
        type:Number,
        required:true
    },
    higher_edu:{
        type:Boolean,
        required:true
    },
    branch_12:{
        type:String
    },
    per_12:{
        type:Number
    },
    diploma_branch:{
        type:String
    },
    diploma_per:{
        type:Number
    },
    jee_rank:{
        type:Number,
        required:true
    },
    State:{
        type:String,
        required:true
    },
    City:{
        type:String,
        required:true
    },
    interest:{
        type:Object,
        default:{}
    }
});

const Register = mongoose.model('Register',register_schema);
module.exports = Register;