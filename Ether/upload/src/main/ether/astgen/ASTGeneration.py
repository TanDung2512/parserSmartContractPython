from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

def flatten(lst):
    list_final = []
    for sublist in lst:
        if isinstance(sublist,list):
            for i in sublist:
                list_final.append(i)
        else:
            list_final.append(sublist)

    return list_final

class ASTGeneration(MPVisitor):
    
    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.declaration()]))

    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        if (ctx.var_declaration()) is not None:
            return self.visit(ctx.var_declaration())
        if (ctx.function_declaration()) is not None :
            return self.visit(ctx.function_declaration())
        if (ctx.procedure_declaration()) is not None:
            return self.visit(ctx.procedure_declaration())

    # Visit a parse tree produced by MPParser#var_declaration.
    def visitVar_declaration(self, ctx:MPParser.Var_declarationContext):
        #return [VarDecl(Id(x),self.visit(ctx.return_type())) for x in ctx.ID().getText() ]
        return self.visit(ctx.var_declaration_more())


    def visitVar_declaration_more(self, ctx:MPParser.Var_declaration_moreContext):
        idlist = [self.visit(x) for x in ctx.idlist()] # [[],[],[]] list of list of ID
        var_type = [self.visit(x) for x in ctx.var_type()] # [] list of type
        # return [VarDecl(x,y) for y in var_type for sub_idlist in idlist for x in sub_idlist]
        list_return = []
        num_of_varType = len(ctx.var_type())
        for i in range(0,num_of_varType):
            for x in idlist[i]:
                list_return.append(VarDecl(x,var_type[i]))
        return list_return


    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitVar_type(self, ctx:MPParser.Var_typeContext):
        return self.visit(ctx.array()) if ctx.array() is not None else self.visit(ctx.primitive_type())


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        if (ctx.INTTYPE() is not None):
            return IntType()
        elif (ctx.BOOLTYPE() is not None):
            return BoolType()
        elif (ctx.REALTYPE() is not None):
            return FloatType()
        elif (ctx.STRINGTYPE() is not None):
            return StringType()


    # Visit a parse tree produced by MPParser#array.
    def visitArray(self, ctx:MPParser.ArrayContext):
        num_of_negative = 0
        num_of_negative = len(ctx.SUBSTRACT())
        if num_of_negative == 0:
            lower = int(ctx.INTLIT(0).getText())
            upper = int(ctx.INTLIT(1).getText())
        elif num_of_negative == 1:
            if ctx.getChild(2).getText() == "-":
                lower = -int(ctx.INTLIT(0).getText())
                upper = int(ctx.INTLIT(1).getText())
            else:
                lower = int(ctx.INTLIT(0).getText())
                upper = -int(ctx.INTLIT(1).getText())
        elif num_of_negative == 2:
            lower = -int(ctx.INTLIT(0).getText())
            upper = -int(ctx.INTLIT(1).getText())

        return  ArrayType(lower,upper,self.visit(ctx.primitive_type()))
        #return ArrayType(int(ctx.INTLIT(0).getText()), int(ctx.INTLIT(1).getText()),self.visit(ctx.primitive_type()))


    # Visit a parse tree produced by MPParser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:MPParser.Procedure_declarationContext):
        if ctx.param_list() is not None:
            param = self.visit(ctx.param_list())
        else:
            param = []

        if ctx.var_declaration() is not None:
            local_var = self.visit(ctx.var_declaration())
        else:
            local_var = []

        body =  self.visit(ctx.compound_stmt())
        #return FuncDecl(Id(ctx.ID().getText()),param,local_var,body)
        return FuncDecl(Id(ctx.ID().getText()),param,local_var,body)


    # Visit a parse tree produced by MPParser#function_declaration.
    def visitFunction_declaration(self, ctx:MPParser.Function_declarationContext):
        if ctx.param_list() is not None:
            param = self.visit(ctx.param_list())
        else:
            param = []

        if ctx.var_declaration() is not None:
            local_var = self.visit(ctx.var_declaration())        
        else:
            local_var = []

        body =  self.visit(ctx.compound_stmt())
        return FuncDecl(Id(ctx.ID().getText()),param,local_var,body,self.visit(ctx.var_type()))


    # Visit a parse tree produced by MPParser#param_list.
    def visitParam_list(self, ctx:MPParser.Param_listContext):
        list_of_parameter = [self.visit(x) for x in ctx.parameter()] # [[],[],[],[]] list of list
        return [x for sub_param_list in list_of_parameter for x in sub_param_list]


    # Visit a parse tree produced by MPParser#parameter.
    def visitParameter(self, ctx:MPParser.ParameterContext):
        idlist = self.visit(ctx.idlist())
        var_type = self.visit(ctx.var_type())
        return [VarDecl(x,var_type) for x in idlist]



    # Visit a parse tree produced by MPParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MPParser.Compound_stmtContext):
        #return [],[self.visit(ctx.statement())] if ctx.statement() else []
        return flatten([self.visit(x) for x in ctx.statement()])


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        if ctx.assign_stmt() is not None:
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt() is not None:
            return self.visit(ctx.if_stmt())
        elif ctx.while_stmt() is not None:
            return self.visit(ctx.while_stmt())
        elif ctx.for_stmt() is not None:
            return self.visit(ctx.for_stmt())
        elif ctx.with_stmt() is not None:
            return self.visit(ctx.with_stmt())
        elif ctx.call_stmt() is not None:
            return self.visit(ctx.call_stmt())
        elif ctx.compound_stmt() is not None:
            return self.visit(ctx.compound_stmt())
        elif ctx.return_stmt() is not None:
            return self.visit(ctx.return_stmt())
        elif ctx.break_stmt() is not None:
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt() is not None:
            return self.visit(ctx.continue_stmt())


    # Visit a parse tree produced by MPParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MPParser.Assign_stmtContext):
        list_of_assign = []
        for i in range(0,len(ctx.lhs()) - 1):
            list_of_assign.append(Assign(self.visit(ctx.lhs(i)), self.visit(ctx.lhs(i+1))))
        list_of_assign.append(Assign(self.visit(ctx.lhs(len(ctx.lhs()) - 1)), self.visit(ctx.expression())))
        return list_of_assign[::-1] # Reverse list

    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() is not None else self.visit(ctx.index_expression())

    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        return If(self.visit(ctx.expression()),
                  flatten([self.visit(ctx.statement(0))]),
                  flatten([self.visit(ctx.statement(1))]) if ctx.ELSE() is not None else [])


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        return While(self.visit(ctx.expression()), flatten([self.visit(ctx.statement())]))
        


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        return For(Id(ctx.ID().getText()),
                      self.visit(ctx.expression(0)),
                      self.visit(ctx.expression(1)),
                      True if ctx.TO() is not None else False,
                      flatten([self.visit(ctx.statement())]))


    # Visit a parse tree produced by MPParser#break_stmt.
    def visitBreak_stmt(self, ctx:MPParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MPParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        return Continue()

    # Visit a parse tree produced by MPParser pass_stmt.
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() is not None else Return(None)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return With(flatten([self.visit(ctx.var_declaration_more())]), flatten([self.visit(ctx.statement())]))


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.expression()])


    # Visit a parse tree produced by MPParser#invocation_expression.
    def visitInvocation_expression(self, ctx:MPParser.Invocation_expressionContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.expression_list()) if ctx.expression_list() is not None else [])


    # Visit a parse tree produced by MPParser#expression_list.
    def visitExpression_list(self, ctx:MPParser.Expression_listContext):
        return [self.visit(x) for x in ctx.expression()]



    # Visit a parse tree produced by MPParser#expression_1.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        if (ctx.AND() is not None and ctx.THEN() is not None):
            return BinaryOp((str("andthen")),
                            self.visit(ctx.expression()),
                            self.visit(ctx.expression_2()))
        elif (ctx.OR() is not None and ctx.ELSE() is not None):
            return BinaryOp((str("orelse")),
                            self.visit(ctx.expression()),
                            self.visit(ctx.expression_2()))
        else:
            return self.visit(ctx.expression_2())

    # Visit a parse tree produced by MPParser#expression_2.
    def visitExpression_2(self, ctx:MPParser.Expression_2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_3(0)),
                            self.visit(ctx.expression_3(1)))
        else:
            return self.visit(ctx.expression_3(0))


    # Visit a parse tree produced by MPParser#expression_3.
    def visitExpression_3(self, ctx:MPParser.Expression_3Context):
        if ctx.expression_3() is not None:
            return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_3()),
                            self.visit(ctx.expression_4()))
        else:
            return self.visit(ctx.expression_4())


    # Visit a parse tree produced by MPParser#expression_4.
    def visitExpression_4(self, ctx:MPParser.Expression_4Context):
        if ctx.expression_4() is not None:
             return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_4()),
                            self.visit(ctx.expression_5()))
        else:
            return self.visit(ctx.expression_5())


    # Visit a parse tree produced by MPParser#expression_5.
    def visitExpression_5(self, ctx:MPParser.Expression_5Context):
        if ctx.expression_5() is not None:
            return UnaryOp((ctx.getChild(0).getText()), self.visit(ctx.expression_5()))
        else:
            return self.visit(ctx.expression_6())


    # Visit a parse tree produced by MPParser#expression_6.
    def visitExpression_6(self, ctx:MPParser.Expression_6Context):
        if ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.ID() is not None:
            return Id(ctx.ID().getText())
        elif ctx.invocation_expression() is not None:
            return self.visit(ctx.invocation_expression())
        elif ctx.TRUE() is not None or ctx.FALSE() is not None:
            return BooleanLiteral(ctx.getChild(0).getText().lower().capitalize())
        elif ctx.INTLIT() is not None:
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REAL_LIT() is not None:
            return FloatLiteral(float(ctx.REAL_LIT().getText()))
        elif ctx.STRING_LIT() is not None:
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.index_expression() is not None:
            return self.visit(ctx.index_expression())


    # Visit a parse tree produced by MPParser#index_expression.
    def visitIndex_expression(self, ctx:MPParser.Index_expressionContext):
        return ArrayCell(self.visit(ctx.index_expression()),self.visit(ctx.expression()) if ctx.expression() is not None else None) if ctx.index_expression() is not None else ArrayCell(self.visit(ctx.expression_no_index_1()),self.visit(ctx.expression()))

    # Visit a parse tree produced by MPParser#expression_no_index_1.
    def visitExpression_no_index_1(self, ctx:MPParser.Expression_no_index_1Context):
        if (ctx.AND() is not None and ctx.THEN() is not None):
            return BinaryOp((str("andthen")),
                            self.visit(ctx.expression_no_index_1()),
                            self.visit(ctx.expression_no_index_2()))
        elif (ctx.OR() is not None and ctx.ELSE() is not None):
            return BinaryOp((str("orelse")),
                            self.visit(ctx.expression_no_index_1()),
                            self.visit(ctx.expression_no_index_2()))
        else:
            return self.visit(ctx.expression_no_index_2())



    # Visit a parse tree produced by MPParser#expression_no_index_2.
    def visitExpression_no_index_2(self, ctx:MPParser.Expression_no_index_2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_no_index_3(0)),
                            self.visit(ctx.expression_no_index_3(1)))
        else:
            return self.visit(ctx.expression_no_index_3(0))


    # Visit a parse tree produced by MPParser#expression_no_index_3.
    def visitExpression_no_index_3(self, ctx:MPParser.Expression_no_index_3Context):
        if ctx.expression_no_index_3() is not None:
            return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_no_index_3()),
                            self.visit(ctx.expression_no_index_4()))
        else:
            return self.visit(ctx.expression_no_index_4())



    # Visit a parse tree produced by MPParser#expression_no_index_4.
    def visitExpression_no_index_4(self, ctx:MPParser.Expression_no_index_4Context):
        if ctx.expression_no_index_4() is not None:
             return BinaryOp((ctx.getChild(1).getText()),
                            self.visit(ctx.expression_no_index_4()),
                            self.visit(ctx.expression_no_index_5()))
        else:
            return self.visit(ctx.expression_no_index_5())


    # Visit a parse tree produced by MPParser#expression_no_index_5.
    def visitExpression_no_index_5(self, ctx:MPParser.Expression_no_index_5Context):
        if ctx.expression_no_index_5() is not None:
            return UnaryOp((ctx.getChild(0).getText()), self.visit(ctx.expression_no_index_5()))
        else:
            return self.visit(ctx.expression_no_index_6())



    # Visit a parse tree produced by MPParser#expression_no_index_6.
    def visitExpression_no_index_6(self, ctx:MPParser.Expression_no_index_6Context):
        if ctx.expression_no_index_1() is not None:
            return self.visit(ctx.expression_no_index_1())
        elif ctx.ID() is not None:
            return Id(ctx.ID().getText())
        elif ctx.invocation_expression() is not None:
            return self.visit(ctx.invocation_expression())
        elif ctx.TRUE() is not None or ctx.FALSE() is not None:
            return BooleanLiteral(ctx.getChild(0).getText().lower().capitalize())
        elif ctx.INTLIT() is not None:
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REAL_LIT() is not None:
            return FloatLiteral(float(ctx.REAL_LIT().getText()))
        elif ctx.STRING_LIT() is not None:
            return StringLiteral(ctx.STRING_LIT().getText())
