import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import api from '../api/Api';
import { fetchItems } from '../actions/action-items';
import Price from './Price';
import Name from './Name';
import Category from './Category';

export class TransferTableRow extends Component {
  /*
   * This component list stock transfers in rows
   * Props:
   *  instance: (Required) An object with stock transfer details
   *         Array of items to be rendered in transfered item table
   *  Usage: <TransferTableRow
   *            instance={object}
   *          />
   * */
  constructor(props) {
    super(props);
    this.state = {
      controlId: 'control',
      collapse: 'collapse',
      showDelete: false
    };
  }
  goTo = (url) => {
    window.location.href = url;
  }
  toggleDelete = () => {
    this.setState({showDelete: true});
    // reset delete confimartion
    setTimeout(() => {
      this.setState({showDelete: false});
    }, 3000);
  }
  deleteInstance = () => {
    api.destroy('/menu/api/delete/' + this.props.instance.id + '/')
    .then((response) => {
      this.props.fetchItems();
    })
    .catch((error) => {
      console.error(error);
    });
  }
  render() {
    var instance = { ...this.props.instance };
    return (
      <tr>
        <td>
          <Category instance={instance}/>
        </td>
        <td>
          <Name instance={instance} />
        </td>
        <td>
          <Price instance={instance} />
        </td>
        <td className="text-center">
          <ul className="icons-list">
            <li className="dropdown">
              { this.state.showDelete &&
                <button onClick={this.deleteInstance} type="button" aria-expanded="true" className="animated fadeIn btn btn-md bg-danger btn-primary dropdown-toggle legitRipple">
                Confirm Delete
              </button>
              }
              {!this.state.showDelete &&
                <button type="button" data-toggle="dropdown" aria-expanded="true" className="animated fadeIn btn btn-md btn-primary dropdown-toggle legitRipple">
                Actions <span className="caret"></span>
                </button>
              }
              <ul className="dropdown-menu dropdown-menu-right">
                <li>
                  <a onClick={this.toggleDelete} href="javascript:;">
                    <i className=" icon-trash-alt"></i> DELETE
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </td>
    </tr>
    );
  }
}

TransferTableRow.propTypes = {
  instance: PropTypes.object.isRequired,
  fetchItems: PropTypes.func.isRequired
};

const mapStateToProps = (state) => ({});

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({
    fetchItems
  }, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(TransferTableRow);
