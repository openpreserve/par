package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@SuppressWarnings("unused")
public class Action {
    @SerializedName("optionalInputs")
    private List<InputItem> optionalInputs = null;

    @SerializedName("outputsRetrieved")
    private List<OutputItem> outputsRetrieved = null;

    @SerializedName("preservationAction")
    private ParIdentifier preservationAction = null;

    @SerializedName("priority")
    private Integer priority = null;

    public void addOptionalInputsItem(InputItem optionalInputsItem) {
        if (this.optionalInputs == null) {
            this.optionalInputs = new ArrayList<>();
        }
        this.optionalInputs.add(optionalInputsItem);
    }

    /**
     * Get optionalInputs
     * @return optionalInputs
     **/
    @ApiModelProperty(value = "")
    public List<InputItem> getOptionalInputs() {
        return optionalInputs;
    }

    public void setOptionalInputs(List<InputItem> optionalInputs) {
        this.optionalInputs = optionalInputs;
    }

    public void addOutputsRetrievedItem(OutputItem outputsRetrievedItem) {
        if (this.outputsRetrieved == null) {
            this.outputsRetrieved = new ArrayList<>();
        }
        this.outputsRetrieved.add(outputsRetrievedItem);
    }

    /**
     * Get outputsRetrieved
     * @return outputsRetrieved
     **/
    @ApiModelProperty(value = "")
    public List<OutputItem> getOutputsRetrieved() {
        return outputsRetrieved;
    }

    public void setOutputsRetrieved(List<OutputItem> outputsRetrieved) {
        this.outputsRetrieved = outputsRetrieved;
    }

    /**
     * Get preservationAction
     * @return preservationAction
     **/
    @ApiModelProperty(required = true, value = "")
    public ParIdentifier getPreservationAction() {
        return preservationAction;
    }

    public void setPreservationAction(ParIdentifier preservationAction) {
        this.preservationAction = preservationAction;
    }

    /**
     * Get priority
     * @return priority
     **/
    @ApiModelProperty(value = "")
    public Integer getPriority() {
        return priority;
    }

    public void setPriority(Integer priority) {
        this.priority = priority;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Action action = (Action) o;
        return Objects.equals(this.optionalInputs, action.optionalInputs) &&
                Objects.equals(this.outputsRetrieved, action.outputsRetrieved) &&
                Objects.equals(this.preservationAction, action.preservationAction) &&
                Objects.equals(this.priority, action.priority);
    }

    @Override
    public int hashCode() {
        return Objects.hash(optionalInputs, outputsRetrieved, preservationAction, priority);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class Action {\n");

        sb.append("    optionalInputs: ").append(toIndentedString(optionalInputs)).append("\n");
        sb.append("    outputsRetrieved: ").append(toIndentedString(outputsRetrieved)).append("\n");
        sb.append("    preservationAction: ").append(toIndentedString(preservationAction)).append("\n");
        sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
